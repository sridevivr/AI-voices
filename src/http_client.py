"""Polite HTTP client: descriptive User-Agent, per-host rate limit, robots.txt, retries."""
from __future__ import annotations

import sys
import time
import urllib.robotparser
from urllib.parse import urlparse

import requests

from .config import PER_HOST_DELAY, REQUEST_TIMEOUT, USER_AGENT

RATE_LIMIT_RETRIES = 6  # waits 30, 60, 120, 240, 300, 300 s (≈17 min) unless Retry-After says otherwise


class RobotsDisallowed(Exception):
    pass


class PoliteSession:
    def __init__(self, per_host_delay: float = PER_HOST_DELAY):
        self.s = requests.Session()
        self.s.headers["User-Agent"] = USER_AGENT
        self.per_host_delay = per_host_delay
        self._last: dict[str, float] = {}
        self._robots: dict[str, urllib.robotparser.RobotFileParser | None] = {}

    # -- robots.txt --------------------------------------------------------
    def _robots_for(self, url: str):
        p = urlparse(url)
        base = f"{p.scheme}://{p.netloc}"
        if base not in self._robots:
            rp = urllib.robotparser.RobotFileParser()
            try:
                r = self._raw_get(f"{base}/robots.txt")
                if r.status_code == 200 and "text/plain" in r.headers.get("content-type", ""):
                    rp.parse(r.text.splitlines())
                else:  # no robots.txt (or an HTML 404 page) -> allow all
                    rp.parse([])
            except requests.RequestException:
                rp.parse([])
            self._robots[base] = rp
        return self._robots[base]

    def allowed(self, url: str) -> bool:
        return self._robots_for(url).can_fetch(USER_AGENT, url)

    # -- requests ----------------------------------------------------------
    def _throttle(self, host: str):
        wait = self._last.get(host, 0) + self.per_host_delay - time.monotonic()
        if wait > 0:
            time.sleep(wait)
        self._last[host] = time.monotonic()

    def _raw_get(self, url: str, **kw) -> requests.Response:
        self._throttle(urlparse(url).netloc)
        return self.s.get(url, timeout=REQUEST_TIMEOUT, **kw)

    def get(self, url: str, retries: int = 3, check_robots: bool = True, **kw) -> requests.Response:
        if check_robots and not self.allowed(url):
            raise RobotsDisallowed(url)
        delay = 5.0
        rate_limited = 0
        attempt = 0
        while True:
            try:
                r = self._raw_get(url, **kw)
            except requests.RequestException:
                if attempt == retries:
                    raise
                attempt += 1
                time.sleep(delay)
                delay *= 2
                continue
            # 429: back off patiently (Substack rate-limits residential IPs for minutes).
            if r.status_code == 429 and rate_limited < RATE_LIMIT_RETRIES:
                rate_limited += 1
                ra = r.headers.get("Retry-After")
                wait = float(ra) if ra and ra.isdigit() else min(30.0 * 2 ** (rate_limited - 1), 300.0)
                print(f"  … 429 from {urlparse(url).netloc}; waiting {wait:.0f}s "
                      f"({rate_limited}/{RATE_LIMIT_RETRIES})", file=sys.stderr)
                time.sleep(wait)
                continue
            if r.status_code in (500, 502, 503, 504) and attempt < retries:
                attempt += 1
                time.sleep(delay)
                delay *= 2
                continue
            return r
