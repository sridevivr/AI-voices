"""Render the insight reports as one self-contained, visual web page: data/out/insights/site/index.html.

Called by `python -m src.insights site` (free: reads pack.json + replies.json, no API calls).
Views (hash routes): #state, #debates, #trends, #tools, #voices. App ideas and the raw numbers are not on the
page; they live in readable files (app_ideas.md / app_ideas.csv, overview.md).

Layout is derived from the structure of the text, not from exact headings, so a re-run still renders well:
  - key points            -> numbered headline cards (first sentence = headline)
  - paragraphs that start with a **bold label** -> cards titled by the label; "1. ..." labels -> numbered steps
  - debate sections (labels "The question", "Why it matters", "Post angle") -> question, two sides side by side,
    then why it matters and a highlighted post angle
  - method / limits sections -> folded away
Charts come from pack.json: what rose and fell, debate volume, trend lines, hype-spike timeline, tool mentions,
voices. Citations sit behind a small "N sources" toggle on each block.
It follows the claude.ai Artifact page contract (no <html>/<head>/<body> tags; title + style first).
"""
from __future__ import annotations

import html
import json
import math
import re
from pathlib import Path

from .config import now_utc

VIEWS = [  # (hash, nav label, report name)
    ("state", "State of AI", "state_of_ai"),
    ("debates", "Debates", "debates"),
    ("trends", "Trends", "trends"),
    ("tools", "Tools", "tools_guide"),
]  # Voices taken off the page 2026-11-22 (owner); voices.md is still written

CSS = """
/* Layout: sticky left index of reports beside a wide content column of cards and charts; on phones the index
   becomes a sticky scrolling tab bar. Prose is chunked into cards; numbers and labels use the mono face. */
:root {
  --bg: #f5f7f9; --surface: #ffffff; --fg: #141a21; --muted: #586474; --line: #dce2e8;
  --accent: #0e6b63; --accent-soft: #e2f1ef; --side: #3d5a99; --side-soft: #e6ebf6;
  --up: #1d7a3c; --up-soft: #e3f3e8; --down: #b2442c; --down-soft: #f8e7e2; --mixed: #86691a; --mixed-soft: #f5efdc;
  --display: "Bricolage Grotesque", "Space Grotesk", system-ui, sans-serif;
  --body: "Inter", system-ui, -apple-system, "Segoe UI", sans-serif;
  --mono: "JetBrains Mono", ui-monospace, "SF Mono", Menlo, monospace;
}
@media (prefers-color-scheme: dark) { :root:not([data-theme="light"]) {
  --bg: #0e1215; --surface: #151b20; --fg: #e6eaee; --muted: #98a3af; --line: #26303a;
  --accent: #52c3b5; --accent-soft: #15302d; --side: #93aee6; --side-soft: #1b2438;
  --up: #63c584; --up-soft: #163122; --down: #f08e76; --down-soft: #3a1e18; --mixed: #dbb64e; --mixed-soft: #332a12;
  color-scheme: dark; } }
:root[data-theme="dark"] {
  --bg: #0e1215; --surface: #151b20; --fg: #e6eaee; --muted: #98a3af; --line: #26303a;
  --accent: #52c3b5; --accent-soft: #15302d; --side: #93aee6; --side-soft: #1b2438;
  --up: #63c584; --up-soft: #163122; --down: #f08e76; --down-soft: #3a1e18; --mixed: #dbb64e; --mixed-soft: #332a12;
  color-scheme: dark; }
* { box-sizing: border-box; }
body { background: var(--bg); color: var(--fg); font: 16px/1.6 var(--body); }
a { color: var(--accent); }
a:focus-visible, summary:focus-visible { outline: 2px solid var(--accent); outline-offset: 2px; border-radius: 4px; }
.shell { display: grid; grid-template-columns: 220px minmax(0, 1fr); gap: 44px; max-width: 1240px; margin: 0 auto;
  padding-left: max(16px, env(safe-area-inset-left, 0px)); padding-right: max(16px, env(safe-area-inset-right, 0px));
  padding-block: 40px 64px; }
.side { position: sticky; top: calc(env(safe-area-inset-top, 0px) + 24px); align-self: start; display: grid; gap: 24px; }
.brand { display: grid; gap: 6px; }
.brand h1 { font: 700 26px/1.1 var(--display); margin: 0; letter-spacing: -0.01em; }
.brand p { margin: 0; color: var(--muted); font-size: 13px; line-height: 1.45; }
.nav { display: grid; gap: 2px; }
.nav a { display: flex; justify-content: space-between; gap: 8px; padding: 8px 12px; border-radius: 8px; color: var(--fg);
  text-decoration: none; font-weight: 500; font-size: 15px; }
.nav a:hover { background: var(--surface); }
.nav a[aria-current="page"] { background: var(--accent-soft); color: var(--accent); }
.nav .n { font: 12px/1.9 var(--mono); color: var(--muted); }
.facts { display: grid; gap: 4px; font: 12px/1.5 var(--mono); color: var(--muted); border-top: 1px solid var(--line); padding-top: 16px; }
.facts b { color: var(--fg); font-weight: 600; }
main { min-width: 0; }
.view { display: grid; gap: 36px; }
.view[hidden] { display: none; }
.view > header { display: grid; gap: 12px; max-width: 76ch; }
.eyebrow { font: 600 12px/1 var(--mono); text-transform: uppercase; letter-spacing: 0.08em; color: var(--accent); }
.view h2 { font: 700 clamp(28px, 4vw, 40px)/1.1 var(--display); margin: 0; text-wrap: balance; letter-spacing: -0.015em; }
.dek { font-size: 19px; line-height: 1.5; color: var(--muted); margin: 0; }
.meta { font: 12px/1.5 var(--mono); color: var(--muted); }
section.s { display: grid; gap: 16px; }
section.s > h3 { font: 650 23px/1.25 var(--display); margin: 0; text-wrap: balance; }
.lede { margin: 0; color: var(--muted); max-width: 76ch; }
.prose { display: grid; gap: 12px; max-width: 76ch; }
.prose p, .card p, .debate p, .step p { margin: 0; }
.prose ul, .prose ol, .card ul, .card ol { margin: 0; padding-left: 20px; display: grid; gap: 4px; }
/* cards */
.cards { display: grid; grid-template-columns: repeat(auto-fill, minmax(280px, 1fr)); gap: 14px; align-items: start; }
.cards.two { grid-template-columns: repeat(auto-fill, minmax(340px, 1fr)); }
.card { background: var(--surface); border: 1px solid var(--line); border-radius: 12px; padding: 16px 18px; display: grid;
  gap: 8px; min-width: 0; font-size: 15px; line-height: 1.55; }
.card h4 { margin: 0; font: 650 17px/1.3 var(--display); text-wrap: balance; }
.kicker { display: block; font: 600 11px/1.3 var(--mono); text-transform: uppercase; letter-spacing: 0.07em; color: var(--muted); margin-bottom: 4px; }
.kp { display: grid; grid-template-columns: repeat(auto-fill, minmax(260px, 1fr)); gap: 14px; align-items: start; }
.kp .card { border-top: 3px solid var(--accent); }
.kp .num { font: 600 13px/1 var(--mono); color: var(--accent); }
.kp h4 { font-size: 18px; }
.kp p { color: var(--muted); font-size: 14.5px; }
.steps { display: grid; gap: 10px; counter-reset: none; }
.step { display: grid; grid-template-columns: 40px minmax(0, 1fr); gap: 14px; background: var(--surface); border: 1px solid var(--line);
  border-radius: 12px; padding: 14px 16px; align-items: start; font-size: 15px; }
.step .badge { width: 32px; height: 32px; border-radius: 50%; background: var(--accent-soft); color: var(--accent);
  display: grid; place-items: center; font: 600 14px/1 var(--mono); }
.step h4 { margin: 0 0 4px; font: 650 16.5px/1.3 var(--display); }
.step p { margin: 0; }
/* debates */
.debate { background: var(--surface); border: 1px solid var(--line); border-radius: 14px; padding: 20px; display: grid; gap: 14px; }
.debate h4 { margin: 0; font: 650 21px/1.25 var(--display); text-wrap: balance; }
.debate .q { margin: 0; color: var(--muted); }
.vs { display: grid; grid-template-columns: minmax(0, 1fr) auto minmax(0, 1fr); gap: 12px; align-items: stretch; }
.vs .sidebox { border-radius: 10px; padding: 14px; display: grid; gap: 4px; align-content: start; font-size: 15px; }
.vs .sidebox.a { background: var(--accent-soft); }
.vs .sidebox.b { background: var(--side-soft); }
.vs .sidebox .kicker { color: var(--accent); }
.vs .sidebox.b .kicker { color: var(--side); }
.vs .v { align-self: center; font: 700 13px/1 var(--mono); color: var(--muted); }
.extra { display: grid; gap: 10px; font-size: 15px; }
.extra > div, .why { display: grid; gap: 2px; }
.post { border-left: 3px solid var(--accent); background: var(--bg); border-radius: 0 10px 10px 0; padding: 12px 14px; font-size: 15px; }
.post .kicker { color: var(--accent); }
/* sources toggle */
details.src { font-size: 12px; }
details.src summary { cursor: pointer; font: 12px/1.6 var(--mono); color: var(--muted); list-style: none; display: inline-block; }
details.src summary::-webkit-details-marker { display: none; }
details.src summary::before { content: "▸ "; }
details.src[open] summary::before { content: "▾ "; }
.cites { display: flex; flex-wrap: wrap; gap: 6px; margin-top: 6px; }
.cite { font: 11px/1.6 var(--mono); padding: 0 7px; border-radius: 999px; border: 1px solid var(--line); color: var(--muted);
  text-decoration: none; white-space: nowrap; background: var(--surface); }
.cite:hover { color: var(--accent); border-color: var(--accent); }
details.more { background: var(--surface); border: 1px solid var(--line); border-radius: 12px; padding: 12px 16px; }
details.more > summary { cursor: pointer; font-weight: 600; color: var(--accent); }
details.more[open] > summary { margin-bottom: 12px; }
/* charts */
.chart { background: var(--surface); border: 1px solid var(--line); border-radius: 12px; padding: 18px; display: grid; gap: 12px; min-width: 0; }
.chart h4 { margin: 0; font: 650 17px/1.3 var(--display); }
.chart .note { font-size: 13px; color: var(--muted); margin: 0; }
.legend { display: flex; flex-wrap: wrap; gap: 12px; font: 12px/1.4 var(--mono); color: var(--muted); }
.legend i { display: inline-block; width: 10px; height: 10px; border-radius: 2px; margin-right: 5px; vertical-align: -1px; }
.div-row { display: grid; grid-template-columns: minmax(110px, 190px) minmax(0, 1fr) 58px; gap: 10px; align-items: center; font-size: 14px; }
.div-track { position: relative; height: 16px; }
.div-track::before { content: ""; position: absolute; left: 50%; top: -4px; bottom: -4px; width: 1px; background: var(--line); }
.div-bar { position: absolute; top: 2px; height: 12px; border-radius: 3px; }
.div-bar.rising { background: var(--up); left: 50%; }
.div-bar.falling { background: var(--down); right: 50%; }
.div-v { font: 12px/1 var(--mono); text-align: right; font-variant-numeric: tabular-nums; color: var(--muted); }
.bars { display: grid; gap: 7px; }
.bar { display: grid; grid-template-columns: minmax(110px, 230px) minmax(0, 1fr) 52px; gap: 12px; align-items: center; font-size: 14px; }
.bar .lbl { min-width: 0; overflow-wrap: anywhere; }
.bar .track { height: 10px; background: var(--bg); border-radius: 999px; overflow: hidden; }
.bar .fill { height: 100%; background: var(--accent); border-radius: 999px; }
.bar .v { font: 13px/1 var(--mono); text-align: right; font-variant-numeric: tabular-nums; color: var(--muted); }
.multiples { display: grid; grid-template-columns: repeat(auto-fill, minmax(190px, 1fr)); gap: 10px; }
.mini { border: 1px solid var(--line); border-radius: 10px; padding: 10px 12px; display: grid; gap: 6px; background: var(--surface); }
.mini .top { display: flex; justify-content: space-between; gap: 8px; align-items: center; font-size: 14px; font-weight: 600; }
.mini .ch { font: 12px/1 var(--mono); color: var(--muted); }
svg.spark { display: block; width: 100%; height: 34px; overflow: visible; }
svg.spark polyline { fill: none; stroke: var(--accent); stroke-width: 1.6; vector-effect: non-scaling-stroke; }
svg.spark .rising polyline, svg.spark polyline.rising { stroke: var(--up); }
svg.spark polyline.falling { stroke: var(--down); }
svg.spark line { stroke: var(--line); stroke-width: 1; vector-effect: non-scaling-stroke; }
.pill { font: 600 10.5px/1 var(--mono); padding: 4px 7px; border-radius: 999px; text-transform: uppercase; letter-spacing: 0.05em; white-space: nowrap; }
.pill.rising { color: var(--up); background: var(--up-soft); }
.pill.falling { color: var(--down); background: var(--down-soft); }
.pill.mixed { color: var(--mixed); background: var(--mixed-soft); }
.pill.flat { color: var(--muted); background: var(--bg); }
.timeline { overflow-x: auto; }
.tl { display: grid; gap: 4px; min-width: 620px; }
.tl-row { display: grid; grid-template-columns: 130px repeat(var(--cols), minmax(0, 1fr)); align-items: center; gap: 2px; font-size: 13px; }
.tl-row .cell { height: 26px; display: grid; place-items: center; border-radius: 4px; }
.tl-row .cell.on { background: var(--accent-soft); }
.tl-dot { border-radius: 50%; background: var(--accent); }
.tl-head .cell { font: 11px/1 var(--mono); color: var(--muted); height: auto; padding-bottom: 4px; }
.tablewrap { overflow-x: auto; }
table { border-collapse: collapse; width: 100%; font-size: 13.5px; }
th, td { text-align: left; padding: 7px 12px; border-bottom: 1px solid var(--line); vertical-align: middle; }
th { font: 600 11px/1.3 var(--mono); text-transform: uppercase; letter-spacing: 0.06em; color: var(--muted); white-space: nowrap; }
td.num { font: 12.5px/1.4 var(--mono); font-variant-numeric: tabular-nums; text-align: right; white-space: nowrap; }
.person .stats { display: flex; flex-wrap: wrap; gap: 6px; align-items: center; }
.tag { font: 11px/1.6 var(--mono); padding: 1px 8px; border-radius: 999px; background: var(--bg); color: var(--muted); }
.count { font: 600 12px/1 var(--mono); color: var(--accent); }
.meter { height: 6px; background: var(--bg); border-radius: 999px; overflow: hidden; }
.meter > span { display: block; height: 100%; background: var(--accent); border-radius: 999px; }
.split { display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 18px; align-items: start; }
.split > div { display: grid; gap: 12px; min-width: 0; }
.split h5 { margin: 0; font: 600 12px/1 var(--mono); text-transform: uppercase; letter-spacing: 0.08em; color: var(--muted); }
footer.f { margin-top: 56px; padding-top: 20px; border-top: 1px solid var(--line); font-size: 13px; color: var(--muted); max-width: 76ch; display: grid; gap: 8px; }
@media (max-width: 900px) {
  .shell { grid-template-columns: minmax(0, 1fr); gap: 20px; padding-block: 16px 48px; }
  .side { position: static; gap: 14px; }
  .nav { position: sticky; top: env(safe-area-inset-top, 0px); z-index: 5; display: flex; overflow-x: auto; gap: 4px;
    background: var(--bg); padding-block: 8px; border-bottom: 1px solid var(--line); }
  .nav a { white-space: nowrap; }
  .nav .n, .facts { display: none; }
  .vs { grid-template-columns: minmax(0, 1fr); }
  .vs .v { justify-self: center; }
  .bar { grid-template-columns: minmax(90px, 130px) minmax(0, 1fr) 44px; }
  .div-row { grid-template-columns: minmax(90px, 120px) minmax(0, 1fr) 48px; }
  body::before { content: ""; position: fixed; inset: 0 0 auto; height: env(safe-area-inset-top, 0px); z-index: 10; background: var(--bg); }
}
@media (prefers-reduced-motion: no-preference) { .view:not([hidden]) { animation: rise .25s ease-out; } }
@keyframes rise { from { transform: translateY(4px); } to { transform: none; } }
"""

JS = """
(function () {
  var ids = %s, start = ids[0];
  function show() {
    var h = (location.hash || "").slice(1); if (ids.indexOf(h) < 0) h = start;
    ids.forEach(function (id) {
      document.getElementById("v-" + id).hidden = id !== h;
      var a = document.querySelector('.nav a[href="#' + id + '"]');
      if (id === h) a.setAttribute("aria-current", "page"); else a.removeAttribute("aria-current");
    });
  }
  window.addEventListener("hashchange", function () { show(); window.scrollTo(0, 0); });
  show();
})();
"""

VENDOR = Path(__file__).parent / "vendor"


def grid_js() -> str:
    """Canvas UI's Grid effect, bundled unmodified with its licence notice (see src/vendor/)."""
    return (VENDOR / "canvas_ui_grid.js").read_text()


# Page effects: big numbers decode once on first view; Grid backdrop behind each report header (desktop + mouse only).
FX_JS = """
(function () {
  var reduce = window.matchMedia("(prefers-reduced-motion: reduce)");
  function decode(b) {
    var final = b.textContent, el = document.createElement("span"), sr = document.createElement("span");
    var t0 = performance.now(), dur = 900, idx = [];
    for (var i = 0; i < final.length; i++) if (/[0-9]/.test(final[i])) idx.push(i);
    sr.className = "sr"; sr.textContent = final; el.className = "dc on"; el.setAttribute("aria-hidden", "true");
    b.textContent = ""; b.appendChild(sr); b.appendChild(el);
    function tick(now) {
      var k = Math.min(1, (now - t0) / dur), settled = Math.floor(k * (idx.length + 1)), out = final.split("");
      for (var j = settled; j < idx.length; j++) out[idx[j]] = String(Math.floor(Math.random() * 10));
      el.textContent = out.join("");
      if (k < 1) requestAnimationFrame(tick); else { el.textContent = final; el.classList.remove("on"); }
    }
    requestAnimationFrame(tick);
  }
  if (!reduce.matches && "IntersectionObserver" in window) {
    var io = new IntersectionObserver(function (es) {
      es.forEach(function (e) { if (e.isIntersecting) { io.unobserve(e.target); decode(e.target); } });
    }, { threshold: 0.6 });
    document.querySelectorAll(".bigstat b").forEach(function (b) { if (/[0-9]/.test(b.textContent)) io.observe(b); });
  }

  var desk = window.matchMedia("(min-width: 901px) and (hover: hover) and (pointer: fine)");
  function accent() {
    var c = getComputedStyle(document.documentElement).getPropertyValue("--accent").trim(), m = /^#([0-9a-f]{6})$/i.exec(c);
    if (!m) return [0.05, 0.42, 0.39];
    var n = parseInt(m[1], 16);
    return [(n >> 16 & 255) / 255, (n >> 8 & 255) / 255, (n & 255) / 255];
  }
  var grids = [];
  function grid() {
    if (!desk.matches || reduce.matches || !window.CanvasUIGrid) return;
    var view = document.querySelector(".view:not([hidden])"), hero = view && view.querySelector(".hero");
    if (!hero || hero.dataset.grid) return;
    hero.dataset.grid = "1";
    try {
      var g = window.CanvasUIGrid.createGrid(
        { source: hero.querySelector(".grid-src"), content: hero.querySelector("header"), output: hero.querySelector(".grid-fx") },
        { tileSize: 34, liftHeight: 14, perspective: 900, amplitude: 1.6, waveSpeed: 0.45, frequency: 11, fadeTime: 0.8,
          shading: 0.5, tint: accent(), tintStrength: 0.45, idleRipples: 4, tilt: 0.6 });
      if (g) grids.push(g);
    } catch (e) {}
  }
  window.matchMedia("(prefers-color-scheme: dark)").addEventListener("change", function () {
    grids.forEach(function (g) { g.setOptions({ tint: accent() }); });
  });
  document.addEventListener("click", function (e) {
    var btn = e.target.closest && e.target.closest(".foldbar button");
    if (!btn) return;
    var open = btn.dataset.fold === "open", view = btn.closest(".view");
    view.querySelectorAll("details.fold").forEach(function (d) { d.open = open; });
  });
  window.addEventListener("hashchange", grid);
  desk.addEventListener("change", grid);
  grid();
})();
"""

esc = lambda s: html.escape(str(s), quote=True)
MONTHS = "Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec".split()


def inline(s: str) -> str:
    s = esc(s)
    s = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", s)
    s = re.sub(r"(?<![\w*])\*(?!\s)(.+?)(?<!\s)\*(?![\w*])", r"<em>\1</em>", s)
    s = re.sub(r"`([^`]+)`", r"<code>\1</code>", s)
    return s


def short_date(d: str) -> str:
    try:
        y, m, dd = d.split("-")
        return f"{MONTHS[int(m) - 1]} {int(dd)}, {y}"
    except (ValueError, IndexError):
        return d


def body_html(text: str) -> str:
    """Paragraph text, which may be a Markdown list."""
    lines = [l for l in text.split("\n") if l.strip()]
    items = [l for l in lines if re.match(r"^\s*(?:[-*]|\d+\.)\s+", l)]
    if items and len(items) == len(lines):
        tag = "ol" if re.match(r"^\s*\d+\.", items[0]) else "ul"
        return f"<{tag}>" + "".join(f"<li>{inline(re.sub(r'^\s*(?:[-*]|\d+\.)\s+', '', l))}</li>" for l in items) + f"</{tag}>"
    return f"<p>{inline(' '.join(lines))}</p>"


class Ctx:
    """Everything a renderer needs: the pack, the reply's allowed evidence, and findings by id."""
    def __init__(self, p, rows_by_fid, allowed):
        self.p, self.rows, self.allowed = p, rows_by_fid, allowed

    def src(self, ids) -> str:
        seen, chips = set(), []
        for i in ids:
            r = self.rows.get(i)
            if i not in self.allowed or not r or r["url"] in seen:
                continue
            seen.add(r["url"])
            chips.append(f'<a class="cite" href="{esc(r["url"])}" target="_blank" rel="noopener" '
                         f'title="{esc(r["summary"])}">{esc(r["source"])} · {esc(short_date(r["date"]))}</a>')
        if not chips:
            return ""
        n = len(chips)
        return f"<details class='src'><summary>{n} source{'s' if n > 1 else ''}</summary><div class='cites'>{''.join(chips)}</div></details>"


LABEL = re.compile(r"^\s*\*\*(.+?)\*\*\s*(.*)$", re.S)


def split_label(text: str):
    """'**Label:** rest' -> ('Label', 'rest'); otherwise (None, text)."""
    m = LABEL.match(text)
    if not m or re.match(r"^(?:[,;]|and\b|or\b|is\b|are\b|was\b|were\b|has\b|have\b)", m.group(2).strip()):
        return None, text
    label = m.group(1).strip().rstrip(":.").strip()
    return label, m.group(2).strip()


def headline(text: str):
    """Split a key point into a first-sentence headline and the rest."""
    parts = re.split(r"(?<=[.!?])\s+(?=[A-Z0-9'\"(])", text.strip(), maxsplit=1)
    return parts[0], (parts[1] if len(parts) > 1 else "")


# ------------------------------------------------------------------ generic blocks
def key_points(reply, ctx) -> str:
    cards = []
    for n, k in enumerate(reply["key_points"], 1):
        h, rest = headline(k["text"])
        cards.append(f"<div class='card'><span class='num'>{n:02d}</span><h4>{inline(h)}</h4>"
                     + (f"<p>{inline(rest)}</p>" if rest else "") + ctx.src(k["evidence_ids"]) + "</div>")
    return f"<section class='s' aria-label='Key points'><div class='kp'>{''.join(cards)}</div></section>"


def section_block(s, ctx, fold=False) -> str:
    paras = s["paragraphs"]
    labeled = [(split_label(pp["text"]), pp) for pp in paras]
    n_lab = sum(1 for (lab, _), _ in labeled if lab)
    head = f"<h3>{inline(s['heading'])}</h3>"
    if fold:
        inner = "".join(body_html(pp["text"]) + ctx.src(pp["evidence_ids"]) for pp in paras)
        return f"<details class='more'><summary>{inline(s['heading'])}</summary><div class='prose'>{inner}</div></details>"
    if paras and n_lab >= max(2, 0.6 * len(paras)):
        numbered = all(re.match(r"^\d+\.", lab) for (lab, _), _ in labeled if lab)
        lead = "".join(f"<p class='lede'>{inline(rest)}</p>{ctx.src(pp['evidence_ids'])}" for (lab, rest), pp in labeled if not lab)
        if numbered:
            items = "".join(
                f"<div class='step'><span class='badge'>{esc(re.match(r'^(\d+)', lab).group(1))}</span><div>"
                f"<h4>{inline(re.sub(r'^\d+\.\s*', '', lab))}</h4>{body_html(rest)}{ctx.src(pp['evidence_ids'])}</div></div>"
                for (lab, rest), pp in labeled if lab)
            return f"<section class='s'>{head}{lead}<div class='steps'>{items}</div></section>"
        cards = "".join(card(lab, rest, pp["evidence_ids"], ctx) for (lab, rest), pp in labeled if lab)
        return f"<section class='s'>{head}{lead}<div class='cards'>{cards}</div></section>"
    inner = "".join(body_html(pp["text"]) + ctx.src(pp["evidence_ids"]) for pp in paras)
    return f"<section class='s'>{head}<div class='prose'>{inner}</div></section>"


def card(label, text, ids, ctx, kicker="") -> str:
    k = f"<span class='kicker'>{esc(kicker)}</span>" if kicker else ""
    return f"<div class='card'>{k}<h4>{inline(label)}</h4>{body_html(text)}{ctx.src(ids)}</div>"


FOLD = re.compile(r"how to read|limits|method|caveat", re.I)


def sections(reply, ctx, skip=()) -> str:
    return "".join(section_block(s, ctx, fold=bool(FOLD.search(s["heading"])))
                   for s in reply["sections"] if s["heading"] not in skip)


# ------------------------------------------------------------------ charts from the pack
def bars(items, unit="", k=12) -> str:
    items = items[:k]
    top = max((v for _, v in items), default=1) or 1
    return "<div class='bars'>" + "".join(
        f"<div class='bar'><span class='lbl'>{esc(n)}</span><div class='track'><div class='fill' style='width:{100 * v / top:.1f}%'></div></div>"
        f"<span class='v'>{v:,}{unit}</span></div>" for n, v in items) + "</div>"


def change_chart(p, k=14, title="What rose and what fell", note="") -> str:
    tr = p["trends"]
    moved = [x for x in tr["domains"] + tr["terms"] if x["verdict"] in ("rising", "falling") and x["findings"] >= 60]
    moved.sort(key=lambda x: -abs(math.log2(x["ratio"])))
    moved = sorted(moved[:k], key=lambda x: -x["ratio"])
    top = max((abs(math.log2(x["ratio"])) for x in moved), default=1) or 1
    rows = "".join(
        f"<div class='div-row'><span>{esc(x['key'])}</span><div class='div-track'>"
        f"<div class='div-bar {x['verdict']}' style='width:{48 * abs(math.log2(x['ratio'])) / top:.1f}%'></div></div>"
        f"<span class='div-v'>×{x['ratio']}</span></div>" for x in moved)
    return (f"<div class='chart'><h4>{esc(title)}</h4><p class='note'>{esc(note or 'Share of findings, ' + p['overview']['trend_periods'] + '. Only changes that most of the six biggest sources show on their own.')}</p>"
            "<div class='legend'><span><i style='background:var(--up)'></i>rising</span><span><i style='background:var(--down)'></i>falling</span></div>"
            f"{rows}</div>")


def sparkline(series: dict, cls="") -> str:
    vals = list(series.values())
    if not vals:
        return ""
    w, h, top = 100, 30, max(vals) or 1
    pts = " ".join(f"{i * w / max(len(vals) - 1, 1):.1f},{h - 2 - (v / top) * (h - 6):.1f}" for i, v in enumerate(vals))
    label = f"{list(series)[0]} to {list(series)[-1]}: " + ", ".join(f"{v:.0f}" for v in vals) + " per 1,000 findings"
    return (f'<svg class="spark" viewBox="0 0 {w} {h}" preserveAspectRatio="none" role="img" aria-label="{esc(label)}">'
            f'<title>{esc(label)}</title><line x1="0" y1="{h - 2}" x2="{w}" y2="{h - 2}"/><polyline class="{cls}" points="{pts}"/></svg>')


def multiples(p, k=16) -> str:
    tr = p["trends"]
    pool = [x for x in tr["terms"] if x["findings"] >= 100]
    pick = [x for x in pool if x["verdict"] in ("rising", "falling")]
    pick += [x for x in sorted(pool, key=lambda x: -x["findings"]) if x not in pick]
    pick = sorted(pick[:k], key=lambda x: (x["verdict"] != "rising", x["verdict"] != "falling", -x["ratio"]))
    cells = "".join(
        f"<div class='mini'><div class='top'><span>{esc(x['key'])}</span><span class='pill {x['verdict']}'>{x['verdict']}</span></div>"
        f"{sparkline(x['monthly_per_1k'], x['verdict'])}<span class='ch'>{x['early_per_1k']} → {x['late_per_1k']} per 1k</span></div>"
        for x in pick)
    return ("<div class='chart'><h4>Topic by topic, month by month</h4><p class='note'>Mentions per 1,000 findings each "
            f"month. Green and red lines passed the trend test.</p><div class='multiples'>{cells}</div></div>")


def spike_timeline(p) -> str:
    sp = p["spikes"]
    if not sp:
        return ""
    months = list(p["trends"]["terms"][0]["monthly_per_1k"])
    cols = len(months)
    head = "<div class='tl-row tl-head'><span></span>" + "".join(
        f"<span class='cell'>{MONTHS[int(m[5:]) - 1]}<br>{m[2:4]}</span>" for m in months) + "</div>"
    top = max(s["peak_per_1k"] for s in sp)
    rows = ""
    for s in sorted(sp, key=lambda s: s["month"]):
        size = 8 + 18 * s["peak_per_1k"] / top
        cells = "".join(
            (f"<span class='cell on' title='{esc(s['term'])}: {s['peak_per_1k']} per 1k in {m} (usual {s['median_per_1k']})'>"
             f"<span class='tl-dot' style='width:{size:.0f}px;height:{size:.0f}px'></span></span>") if m == s["month"]
            else "<span class='cell'></span>" for m in months)
        rows += f"<div class='tl-row'><span>{esc(s['term'])}</span>{cells}</div>"
    return ("<div class='chart'><h4>Hype spikes</h4><p class='note'>Months when a topic ran far above its usual level "
            f"(launches, viral moments). Bigger dot = bigger peak.</p><div class='timeline'><div class='tl' style='--cols:{cols}'>"
            f"{head}{rows}</div></div></div>")


def trend_table(items) -> str:
    rows = "".join(f"<tr><td>{esc(x['key'])}</td><td class='num'>{x['findings']:,}</td>"
                   f"<td class='num'>{x['early_per_1k']} → {x['late_per_1k']}</td><td class='num'>×{x['ratio']}</td>"
                   f"<td class='num'>{x['big_sources_up']} / {x['big_sources_down']}</td>"
                   f"<td><span class='pill {x['verdict']}'>{x['verdict']}</span></td></tr>" for x in items)
    return ("<div class='tablewrap'><table><thead><tr><th>Topic</th><th>Findings</th><th>Early → late per 1k</th><th>Change</th>"
            f"<th>Big sources ↑/↓</th><th>Verdict</th></tr></thead><tbody>{rows}</tbody></table></div>")


def tool_chart(p, k=15) -> str:
    items = list(p["tools"]["counts"].items())[:k]
    return ("<div class='chart'><h4>Most-mentioned tools</h4><p class='note'>Mentions in findings about tools, techniques and "
            "workarounds. These sources lean toward builders and Claude, so read it as what this crowd recommends.</p>"
            f"{bars(items, k=k)}</div>")


def voice_chart(p, k=12) -> str:
    items = [(v["who"], v["findings"]) for v in p["voices"]][:k]
    return ("<div class='chart'><h4>Who drives the conversation</h4><p class='note'>Findings attributed to each person. "
            f"Counts reflect how much each source publishes and quotes, not influence.</p>{bars(items, k=k)}</div>")


def debate_chart(p) -> str:
    items = [(d["title"], d["types"].get("debate", 0)) for d in p["debates"]]
    return ("<div class='chart'><h4>How hotly each topic was argued</h4><p class='note'>Findings where informed people "
            f"publicly disagreed, by theme.</p>{bars(items, k=10)}</div>")


# ------------------------------------------------------------------ report views
def header(eyebrow, reply, p) -> str:
    o = p["overview"]
    return (f"<header><div class='eyebrow'>{esc(eyebrow)}</div><h2>{inline(reply['title'])}</h2>"
            f"<p class='dek'>{inline(reply['dek'])}</p><div class='meta'>{esc(o['window'])} · {o['findings']:,} findings · "
            f"{len(o['sources'])} sources</div></header>")


def state_view(reply, ctx) -> str:
    p = ctx.p
    out, charts_done = [header("State of AI", reply, p), key_points(reply, ctx)], set()
    for s in reply["sections"]:
        h = s["heading"].lower()
        if FOLD.search(h):
            out.append(section_block(s, ctx, fold=True))
            continue
        if "changed" in h and "change" not in charts_done:
            out.append(change_chart(p))
            charts_done.add("change")
        if "struggl" in h:  # split builder vs everyday cards into two columns when labelled that way
            labeled = [(split_label(pp["text"]), pp) for pp in s["paragraphs"]]
            groups = {}
            for (lab, rest), pp in labeled:
                if lab and ":" in lab:
                    g, t = lab.split(":", 1)
                    t = t.strip()
                    groups.setdefault(g.strip(), []).append(card(t[:1].upper() + t[1:], rest, pp["evidence_ids"], ctx))
                else:
                    groups.setdefault("Also", []).append(card(lab or "", rest, pp["evidence_ids"], ctx))
            if len(groups) >= 2:
                cols = "".join(f"<div><h5>{esc(g)}</h5>{''.join(c)}</div>" for g, c in groups.items())
                out.append(f"<section class='s'><h3>{inline(s['heading'])}</h3><div class='split'>{cols}</div></section>")
                continue
        out.append(section_block(s, ctx))
        if ("used" in h or "tool" in h) and "tools" not in charts_done:
            out.append(tool_chart(p, 12))
            charts_done.add("tools")
        if ("drives" in h or "voices" in h or "who" in h) and "voices" not in charts_done:
            out.append(voice_chart(p))
            charts_done.add("voices")
    if "change" not in charts_done:
        out.insert(2, change_chart(p))
    return "".join(out)


DEBATE_Q = re.compile(r"^the question$", re.I)
DEBATE_WHY = re.compile(r"why it matters", re.I)
DEBATE_POST = re.compile(r"post angle", re.I)


def debate_card(s, ctx) -> str:
    q, why, post, sides, extra = None, None, None, [], []
    for pp in s["paragraphs"]:
        lab, rest = split_label(pp["text"])
        ids = pp["evidence_ids"]
        if lab and DEBATE_Q.match(lab):
            q = (rest, ids)
        elif lab and DEBATE_WHY.search(lab):
            why = (rest, ids)
        elif lab and DEBATE_POST.search(lab):
            post = (rest, ids)
        elif lab and len(sides) < 2:
            sides.append((lab, rest, ids))
        else:
            extra.append((lab, rest, ids))
    title = re.sub(r"^\d+\.\s*", "", s["heading"])
    num = re.match(r"^(\d+)\.", s["heading"])
    html_ = f"<article class='debate'><span class='kicker' style='font:600 12px/1 var(--mono);color:var(--muted)'>DEBATE {num.group(1) if num else ''}</span><h4>{inline(title)}</h4>"
    if q:
        html_ += f"<p class='q'>{inline(q[0])}</p>{ctx.src(q[1])}"
    if len(sides) == 2:
        a, b = sides
        html_ += (f"<div class='vs'><div class='sidebox a'><span class='kicker'>{inline(a[0])}</span>{body_html(a[1])}{ctx.src(a[2])}</div>"
                  f"<span class='v'>vs</span><div class='sidebox b'><span class='kicker'>{inline(b[0])}</span>{body_html(b[1])}{ctx.src(b[2])}</div></div>")
    else:
        extra = [(l, r, i) for l, r, i in sides] + extra
    if extra:
        html_ += "<div class='extra'>" + "".join(
            f"<div>{f'<span class=kicker>{inline(l)}</span>' if l else ''}{body_html(r)}{ctx.src(i)}</div>" for l, r, i in extra) + "</div>"
    if why:
        html_ += f"<div class='why'><span class='kicker'>Why it matters</span>{body_html(why[0])}{ctx.src(why[1])}</div>"
    if post:
        html_ += f"<div class='post'><span class='kicker'>Post angle</span>{body_html(post[0])}</div>"
    return html_ + "</article>"


def debates_view(reply, ctx) -> str:
    out = [header("Debates", reply, ctx.p), key_points(reply, ctx), debate_chart(ctx.p)]
    for s in reply["sections"]:
        labs = [split_label(pp["text"])[0] or "" for pp in s["paragraphs"]]
        if any(DEBATE_Q.match(l) for l in labs) or any(DEBATE_POST.search(l) for l in labs):
            out.append(debate_card(s, ctx))
        else:
            out.append(section_block(s, ctx, fold=bool(FOLD.search(s["heading"]))))
    return "".join(out)


def trends_view(reply, ctx) -> str:
    p, tr = ctx.p, ctx.p["trends"]
    out = [header("Trends", reply, p), key_points(reply, ctx), change_chart(p, 16), multiples(p), spike_timeline(p)]
    out.append(sections(reply, ctx))
    out.append("<details class='more'><summary>All the trend data</summary>"
               f"<p class='lede'>Periods: {esc(p['overview']['trend_periods'])}. Rising or falling = a change of 15% or more that "
               "at least four of the six biggest sources show on their own, with at most one against.</p>"
               "<h4>Domains</h4>" + trend_table(tr["domains"]) + "<h4>Finding types</h4>" + trend_table(tr["types"])
               + "<h4>Terms (50+ findings, keyword matches)</h4>" + trend_table([x for x in tr["terms"] if x["findings"] >= 50])
               + "</details>")
    return "".join(out)


def tools_view(reply, ctx) -> str:
    out = [header("Tools", reply, ctx.p), key_points(reply, ctx), tool_chart(ctx.p)]
    buf = []  # job cards waiting to be laid out as one grid
    for s in reply["sections"]:
        h = s["heading"]
        if re.match(r"^part\b", h, re.I):  # part divider: heading + short intro, then its job cards
            if buf:
                out.append(f"<div class='cards two'>{''.join(buf)}</div>")
                buf = []
            intro = "".join(f"<p class='lede'>{inline(pp['text'])}</p>" for pp in s["paragraphs"])
            out.append(f"<section class='s'><h3>{inline(h)}</h3>{intro}</section>")
            continue
        m = re.match(r"^job:\s*(.+)$", h, re.I)
        if m:  # each job becomes a card
            inner = "".join(body_html(pp["text"]) + ctx.src(pp["evidence_ids"]) for pp in s["paragraphs"])
            buf.append(f"<div class='card'><span class='kicker'>Job</span><h4>{inline(m.group(1)[0].upper() + m.group(1)[1:])}</h4>{inner}</div>")
            continue
        if buf:
            out.append(f"<div class='cards two'>{''.join(buf)}</div>")
            buf = []
        out.append(section_block(s, ctx, fold=bool(FOLD.search(h))))
    if buf:
        out.append(f"<div class='cards two'>{''.join(buf)}</div>")
    return "".join(out)


def voices_view(reply, ctx) -> str:
    p = ctx.p
    by_name = {v["who"]: v for v in p["voices"]}
    top = max((v["findings"] for v in p["voices"]), default=1)
    out = [header("Voices", reply, p), key_points(reply, ctx), voice_chart(p, 15)]
    for s in reply["sections"]:
        labeled = [(split_label(pp["text"]), pp) for pp in s["paragraphs"]]
        if not any(lab for (lab, _), _ in labeled):
            out.append(section_block(s, ctx, fold=bool(FOLD.search(s["heading"]))))
            continue
        cards = []
        for (lab, rest), pp in labeled:
            if not lab:  # e.g. "**antirez**, **Gergely Orosz** and **Hamel Husain** are smaller voices..."
                names = re.findall(r"\*\*(.+?)\*\*", pp["text"])
                lab = ", ".join(names) if names else ""
            vs = [v for name, v in by_name.items() if lab and (name in lab or name.split()[-1] in lab)]
            stats = ""
            if vs:
                v = vs[0]
                stats = (f"<div class='person'><div class='stats'><span class='count'>{v['findings']:,} findings</span>"
                         + "".join(f"<span class='tag'>{esc(d)}</span>" for d in v["top_domains"][:2])
                         + f"</div><div class='meter'><span style='width:{100 * v['findings'] / top:.0f}%'></span></div></div>")
            cards.append(f"<div class='card'><h4>{inline(lab or '')}</h4>{stats}{body_html(rest)}{ctx.src(pp['evidence_ids'])}</div>")
        out.append(f"<section class='s'><h3>{inline(s['heading'])}</h3><div class='cards two'>{''.join(cards)}</div></section>")
    return "".join(out)


RENDERERS = {"state_of_ai": state_view, "debates": debates_view, "trends": trends_view,
             "tools_guide": tools_view, "voices": voices_view}


def build_site(p: dict, replies: dict, rows_by_fid: dict, from_insights, ideas: dict | None = None) -> str:
    """`ideas` is accepted for compatibility but no longer shown (app ideas live in app_ideas.md / .csv)."""
    o = p["overview"]
    views = [v for v in VIEWS if v[2] in replies]
    nav = "".join(f"<a href='#{h}'><span>{icon(TAB_ICONS.get(h, 'chart'))}{esc(label)}</span><span class='n'>{n:02d}</span></a>"
                  for n, (h, label, _) in enumerate(views, 1))
    PAGE_QUOTES[0] = QuotePicker()
    body = ""
    for h, label, name in views:
        reply = replies[name]
        ctx = Ctx(p, rows_by_fid, set(reply.get("_allowed") or from_insights.allowed_ids(p, name)))
        v2 = bool(reply.get("sections")) and "cards" in reply["sections"][0]
        render_fn = (RENDERERS_V2 if v2 else RENDERERS)[name]
        body += f"<article class='view' id='v-{h}' aria-label='{esc(label)}'>{render_fn(reply, ctx)}</article>"
    kinds = "newsletters, blogs, Hacker News" + (" and Bluesky" if "Bluesky" in o["sources"] else "")
    facts = (f"<div class='facts'><div><b>{o['findings']:,}</b> findings</div><div><b>{len(o['sources'])}</b> sources</div>"
             f"<div><b>{o['items']:,}</b> articles, threads &amp; posts</div><div>{esc(o['window'])}</div></div>")
    return f"""<title>AI Voices 2026</title>
<meta name="claude:viewport-fit-sides" content="cover">
<meta name="description" content="What a year of AI commentary says: the state of AI, debates, trends and tools.">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,600;12..96,700&family=Inter:wght@400;500;600&family=JetBrains+Mono:wght@400;600&display=swap">
<style>{CSS}{CSS2}</style>
<div class="shell">
  <aside class="side">
    <div class="brand"><h1>AI Voices 2026</h1><p>What a year of AI commentary says, from {len(o['sources'])} sources: {kinds}.</p></div>
    <nav class="nav" aria-label="Reports">{nav}</nav>
    {facts}
  </aside>
  <main>
    {body}
    <footer class="f">
      <div>Generated {now_utc():%Y-%m-%d} by the AI Voices pipeline: posts and articles from {len(o['sources'])} public sources,
      findings extracted by Claude Haiku 5.5, grouped into themes and written up by Claude Sonnet 5.5. Every number and chart is
      computed from the findings; every source link is a finding the text cites.</div>
      <div>Limits: the sources lean toward builders and AI insiders; mainstream business press, non-English sources, video and
      social platforms{" (apart from a curated list of Bluesky accounts)" if "Bluesky" in o["sources"] else ""} are not included;
      paid Substack posts were skipped. Counts measure attention, not how many people experience something.</div>
      <div>Header animation: the Grid effect from <a href="https://github.com/DavidHDev/canvas-ui" target="_blank" rel="noopener">Canvas UI</a>,
      Copyright &copy; 2026 David Haz, used under the MIT + Commons Clause licence (use in a website is allowed; the
      component itself may not be sold or redistributed). Motion and number styling are inspired by Canvas UI.</div>
    </footer>
  </main>
</div>
<script>{JS % json.dumps([v[0] for v in views])}</script>
<script>{grid_js()}</script>
<script>{FX_JS}</script>
"""


# ================================================================== v2: short, structured replies
ICON_SVG = {
    "shield": '<path d="M12 3l7 3v5c0 4.5-3 8-7 10-4-2-7-5.5-7-10V6z"/>',
    "coins": '<ellipse cx="12" cy="6.5" rx="7" ry="3"/><path d="M5 6.5v5c0 1.7 3.1 3 7 3s7-1.3 7-3v-5M5 11.5v5c0 1.7 3.1 3 7 3s7-1.3 7-3v-5"/>',
    "terminal": '<rect x="3" y="4" width="18" height="16" rx="2"/><path d="M7 9l3 3-3 3M12.5 15H17"/>',
    "chat": '<path d="M4 5h16v11H9l-5 4z"/>',
    "chart": '<path d="M4 20V11M10 20V5M16 20v-6M21 20H3"/>',
    "bolt": '<path d="M13 2L4 14h7l-1 8 9-12h-7z"/>',
    "wrench": '<path d="M15 4a5 5 0 0 0-5.6 6.6L3 17l4 4 6.4-6.4A5 5 0 0 0 20 9l-3 3-4-4z"/>',
    "bulb": '<path d="M9 18h6M10 21h4M12 3a6 6 0 0 0-4 10.5c.7.7 1 1.5 1 2.5h6c0-1 .3-1.8 1-2.5A6 6 0 0 0 12 3z"/>',
    "book": '<path d="M4 4.5A1.5 1.5 0 0 1 5.5 3H20v15H5.5A1.5 1.5 0 0 0 4 19.5zM4 19.5A1.5 1.5 0 0 0 5.5 21H20"/>',
    "briefcase": '<rect x="3" y="7" width="18" height="13" rx="2"/><path d="M9 7V5h6v2M3 12h18"/>',
    "spark": '<path d="M12 3v5M12 16v5M3 12h5M16 12h5M6 6l3 3M15 15l3 3M6 18l3-3M15 9l3-3"/>',
    "scale": '<path d="M12 4v16M6 20h12M4 8h16M4 8l-2.5 6h5zM20 8l-2.5 6h5z"/>',
    "robot": '<rect x="5" y="8" width="14" height="11" rx="2"/><path d="M12 4v4M9 13h.01M15 13h.01M9 16h6"/>',
    "people": '<circle cx="9" cy="8" r="3.2"/><path d="M3 20c0-3.3 2.7-6 6-6s6 2.7 6 6"/><circle cx="17" cy="9" r="2.6"/><path d="M16 14.2c2.8.4 5 2.8 5 5.8"/>',
}
ICON_RULES = [  # first match wins
    (r"secur|safety|risk|cyber|sandbox|guard|trust|attack", "shield"),
    (r"regulat|polic|govern|liab|law|court|militar|pause|pac", "scale"),
    (r"cost|price|pric|money|bubble|financ|pay|market|quota|subscript|moat|commod|spend|bill", "coins"),
    (r"robot|hardware|gpu|chip|compute|data cent", "robot"),
    (r"learn|educat|student|school|teach|explain", "book"),
    (r"job|career|work|enterprise|team|unemploy|hire|hiring|business", "briefcase"),
    (r"creat|media|design|video|music|image|art|voice|writ|slop", "spark"),
    (r"argu|debat|said|voices|who|people|follow", "chat"),
    (r"trend|rose|rise|fell|fall|change|shift|spike|hype|moment|uncertain|steady", "bolt"),
    (r"tool|use|habit|technique|step|stack", "wrench"),
    (r"cod|build|agent|devtool|engineer|harness|software|program", "terminal"),
    (r"research|model|capabilit|scal|agi|reason|open|conscious|think", "bulb"),
]
TAB_ICONS = {"state": "chart", "debates": "chat", "trends": "bolt", "tools": "wrench", "voices": "people"}


def icon(name: str, cls: str = "ic") -> str:
    return (f'<svg class="{cls}" viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" '
            f'stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round">{ICON_SVG.get(name, ICON_SVG["chart"])}</svg>')


def icon_for(text: str) -> str:
    t = text.lower()
    return next((ic for rx, ic in ICON_RULES if re.search(rx, t)), "chart")


CSS2 = """
.ic { width: 20px; height: 20px; flex: none; color: var(--accent); }
.nav .ic { width: 17px; height: 17px; color: currentColor; opacity: .8; }
.nav a { align-items: center; }
.nav a > span:first-child { display: flex; gap: 9px; align-items: center; }
.sec-head { display: grid; grid-template-columns: minmax(0, 1fr) auto; gap: 18px; align-items: end;
  border-bottom: 1px solid var(--line); padding-bottom: 12px; }
.sec-title { display: grid; gap: 6px; min-width: 0; }
.sec-title h3 { display: flex; gap: 10px; align-items: center; margin: 0; font: 650 23px/1.25 var(--display); }
.sec-title .ic { width: 24px; height: 24px; }
.takeaway { margin: 0; font-size: 17px; color: var(--muted); max-width: 70ch; text-wrap: pretty; }
.bigstat { text-align: right; display: grid; gap: 2px; max-width: 200px; }
.bigstat b { font: 700 clamp(28px, 4vw, 40px)/1 var(--display); color: var(--accent); font-variant-numeric: tabular-nums; }
.bigstat span { font-size: 12.5px; color: var(--muted); line-height: 1.3; }
.card .ch { display: flex; gap: 8px; align-items: center; }
.card .ch .ic { width: 18px; height: 18px; }
.chips { display: flex; flex-wrap: wrap; gap: 5px; }
.chip { font: 500 12px/1.6 var(--body); padding: 0 9px; border-radius: 999px; background: var(--side-soft); color: var(--side); white-space: nowrap; }
.sidebox.a .chip { background: var(--surface); color: var(--accent); }
.sidebox.b .chip { background: var(--surface); color: var(--side); }
figure.pq { margin: 0; padding: 20px 24px; border-radius: 14px; background: var(--accent-soft); display: grid; gap: 10px; max-width: 76ch; }
figure.pq blockquote { margin: 0; font: 600 clamp(19px, 2.4vw, 23px)/1.4 var(--display); text-wrap: pretty; }
figure.pq figcaption { font-size: 13.5px; color: var(--muted); }
figure.pq a { color: inherit; }
.kp2 { display: grid; grid-template-columns: repeat(auto-fill, minmax(240px, 1fr)); gap: 14px; align-items: start; }
.kp2 .card { border-top: 3px solid var(--accent); }
.kp2 .num { font: 600 13px/1 var(--mono); color: var(--accent); }
.kp2 h4 { font-size: 18px; }
.kp2 p { color: var(--muted); font-size: 14.5px; }
.year { overflow-x: auto; }
.year-grid { display: grid; grid-template-columns: repeat(var(--cols), minmax(66px, 1fr)); min-width: 760px; }
@media (max-width: 900px) { .year-grid { min-width: calc(var(--cols) * 84px); } }
.year-col { display: grid; align-content: start; gap: 6px; padding: 0 1px; min-width: 0; border-left: 1px solid var(--line); min-height: 120px; }
.year-col:first-child { border-left: 0; }
.year-col .mo { font: 600 11px/1.2 var(--mono); color: var(--muted); text-transform: uppercase; letter-spacing: .05em; padding: 2px 4px 6px; }
.moment { background: var(--surface); border: 1px solid var(--line); border-left: 2px solid var(--accent); border-radius: 5px;
  padding: 4px 2px 4px 4px; font-size: 11.5px; letter-spacing: -0.01em; line-height: 1.3; hyphens: auto; overflow-wrap: break-word; min-width: 0; }
.heat { overflow-x: auto; }
.heat-grid { display: grid; grid-template-columns: minmax(140px, 200px) repeat(var(--cols), minmax(26px, 1fr)) 70px; gap: 3px; min-width: 700px; align-items: center; font-size: 13px; }
.heat-grid .hd { font: 11px/1.1 var(--mono); color: var(--muted); text-align: center; }
.heat-cell { height: 22px; border-radius: 3px; background: var(--bg); position: relative; overflow: hidden; }
.heat-cell > i { position: absolute; inset: 0; background: var(--accent); }
.heat-grid .pill { justify-self: start; }
.bubwrap { overflow-x: auto; }
svg.bubbles { width: 100%; min-width: 640px; height: auto; display: block; }
svg.bubbles text { fill: var(--fg); font: 11px var(--body); }
svg.bubbles text.ax { fill: var(--muted); font: 11px var(--mono); }
svg.bubbles text.q { fill: var(--muted); font: 600 11px var(--mono); text-transform: uppercase; letter-spacing: .05em; }
svg.bubbles line { stroke: var(--line); }
svg.bubbles circle { stroke: var(--surface); stroke-width: 1; }
svg.bubbles circle.up { fill: var(--up); fill-opacity: .75; }
svg.bubbles circle.down { fill: var(--down); fill-opacity: .7; }
svg.bubbles circle.flat { fill: var(--muted); fill-opacity: .45; }
.vmap { display: grid; grid-template-columns: 26px repeat(5, minmax(0, 1fr)); gap: 4px; }
.vmap .cell { min-height: 64px; border-radius: 8px; background: var(--bg); padding: 6px; display: flex; flex-wrap: wrap; gap: 4px; align-content: flex-start; }
.vmap .cell.mid { background: color-mix(in srgb, var(--bg) 70%, var(--line)); }
.vmap .yl { writing-mode: vertical-rl; transform: rotate(180deg); font: 11px/1.2 var(--mono); color: var(--muted); text-align: center; align-self: center; }
.vmap .xl { grid-column: 2 / -1; display: flex; justify-content: space-between; font: 11px/1.2 var(--mono); color: var(--muted); }
.vname { font: 500 12px/1.5 var(--body); padding: 1px 8px; border-radius: 999px; background: var(--surface); border: 1px solid var(--line); }
.debate2 { background: var(--surface); border: 1px solid var(--line); border-radius: 14px; padding: 20px; display: grid; gap: 14px; }
.debate2 h4 { margin: 0; font: 650 21px/1.25 var(--display); display: flex; gap: 10px; align-items: center; }
.debate2 .q { margin: 0; font-size: 17px; color: var(--muted); }
.debate2 .sidebox h5 { margin: 0; font: 650 15.5px/1.3 var(--display); }
.debate2 .sidebox p, .debate2 .extra p { margin: 0; }
@media (max-width: 900px) {
  .sec-head { grid-template-columns: minmax(0, 1fr); }
  .bigstat { text-align: left; }
  .vmap .cell { min-height: 54px; }
}
""" + """
/* Polish, after Canvas UI's tokens: one easing curve, 120-260ms motion, soft layered shadows, three border strengths. */
:root {
  --ease-out: cubic-bezier(0.23, 1, 0.32, 1);
  --dur-press: 120ms; --dur-fast: 150ms; --dur-base: 200ms; --dur-slide: 260ms;
  --line-subtle: color-mix(in oklab, var(--fg) 7%, transparent);
  --line-strong: color-mix(in oklab, var(--fg) 20%, transparent);
  --shadow-card: 0 1px 2px rgb(0 0 0 / 4%), 0 10px 28px -14px rgb(0 0 0 / 12%);
  --shadow-lift: 0 1px 2px rgb(0 0 0 / 5%), 0 14px 36px -12px rgb(0 0 0 / 18%);
}
@media (prefers-color-scheme: dark) { :root:not([data-theme="light"]) {
  --shadow-card: 0 1px 2px rgb(0 0 0 / 35%), 0 10px 28px -14px rgb(0 0 0 / 70%);
  --shadow-lift: 0 1px 2px rgb(0 0 0 / 40%), 0 14px 36px -12px rgb(0 0 0 / 80%); } }
:root[data-theme="dark"] {
  --shadow-card: 0 1px 2px rgb(0 0 0 / 35%), 0 10px 28px -14px rgb(0 0 0 / 70%);
  --shadow-lift: 0 1px 2px rgb(0 0 0 / 40%), 0 14px 36px -12px rgb(0 0 0 / 80%); }
.card, .chart, .debate, .debate2, .step, details.more { box-shadow: var(--shadow-card); }
.card, .debate2 { transition: box-shadow var(--dur-base) var(--ease-out), border-color var(--dur-base) var(--ease-out),
  transform var(--dur-base) var(--ease-out); }
@media (hover: hover) {
  .card:hover { box-shadow: var(--shadow-lift); border-color: var(--line-strong); transform: translateY(-1px); }
  .kp .card:hover, .kp2 .card:hover { border-top-color: var(--accent); }
}
.nav a { transition: background-color var(--dur-fast) var(--ease-out), color var(--dur-fast) var(--ease-out),
  transform var(--dur-press) var(--ease-out); }
.nav a:active { transform: scale(0.98); }
.cite, details.src summary, details.more > summary { transition: color var(--dur-fast) var(--ease-out), border-color var(--dur-fast) var(--ease-out); }
.year-col, th, td, .heat-grid .hd { border-color: var(--line-subtle); }
.facts, footer.f, .sec-head { border-color: var(--line-subtle); }
.view:not([hidden]) { animation-duration: var(--dur-slide); animation-timing-function: var(--ease-out); }

/* Intro, audience tag, post idea */
.intro { background: var(--surface); border: 1px solid var(--line); border-left: 3px solid var(--accent); border-radius: 12px;
  padding: 18px 20px; display: grid; gap: 10px; box-shadow: var(--shadow-card); max-width: 80ch; }
.intro h3 { margin: 0; font: 650 19px/1.3 var(--display); }
.intro .lead { margin: 0; font-size: 16.5px; }
.intro ul { margin: 0; padding-left: 18px; display: grid; gap: 6px; font-size: 15px; color: var(--muted); }
.intro ul b { color: var(--fg); }
.intro .start { margin: 0; font-weight: 500; }
.aud { display: inline-block; font: 600 10.5px/1 var(--mono); text-transform: uppercase; letter-spacing: .05em; color: var(--side);
  background: var(--side-soft); border-radius: 999px; padding: 4px 8px; margin-left: 4px; vertical-align: middle; white-space: nowrap; }
details.postidea { font-size: 15px; }
details.postidea > summary { cursor: pointer; list-style: none; display: inline-flex; gap: 6px; align-items: center;
  font: 600 12px/1 var(--mono); text-transform: uppercase; letter-spacing: .06em; color: var(--accent); padding: 6px 0; }
details.postidea > summary::-webkit-details-marker { display: none; }
details.postidea > summary::before { content: "+"; font-size: 14px; }
details.postidea[open] > summary::before { content: "−"; }
details.postidea > p { margin: 4px 0 0; border-left: 3px solid var(--accent); background: var(--bg); border-radius: 0 10px 10px 0; padding: 10px 14px; }
.mini .top span:first-child { min-width: 0; overflow-wrap: anywhere; }
@media (max-width: 900px) { .nav a { padding: 8px 10px; font-size: 14.5px; } .nav .ic { display: none; } }

/* Foldable sections and debates */
details.fold > summary { list-style: none; cursor: pointer; border-radius: 10px; }
details.fold > summary::-webkit-details-marker { display: none; }
details.fold > summary:focus-visible { outline: 2px solid var(--accent); outline-offset: 4px; }
.chev { width: 20px; height: 20px; flex: none; margin-left: 2px; color: var(--muted); transform: rotate(-90deg);
  transition: transform var(--dur-base) var(--ease-out), color var(--dur-fast) var(--ease-out); }
details.fold[open] > summary .chev { transform: none; }
details.fold > summary:hover .chev, details.fold > summary:hover h3, details.fold > summary:hover h4 { color: var(--accent); }
details.fold > .fold-body { display: grid; gap: 16px; padding-top: 16px; }
details.fold:not([open]) > summary .sec-head { border-bottom-style: dashed; }
details.debate2 > summary { display: grid; gap: 8px; }
details.debate2:not([open]) { padding-block: 16px; }
details.debate2 > .fold-body { gap: 14px; }
.foldbar { display: flex; gap: 8px; flex-wrap: wrap; margin-top: 4px; }
.foldbar button { font: 500 12.5px/1 var(--mono); color: var(--muted); background: var(--surface); border: 1px solid var(--line);
  border-radius: 999px; padding: 7px 12px; cursor: pointer; transition: color var(--dur-fast) var(--ease-out),
  border-color var(--dur-fast) var(--ease-out), transform var(--dur-press) var(--ease-out); }
.foldbar button:hover { color: var(--accent); border-color: var(--accent); }
.foldbar button:active { transform: scale(0.97); }

/* Big numbers "decode" once when they first scroll into view (skipped with reduced motion). */
.sr { position: absolute; width: 1px; height: 1px; overflow: hidden; clip-path: inset(50%); white-space: nowrap; }
.bigstat b span { font: inherit; color: inherit; line-height: inherit; }
.bigstat b .dc { transition: color var(--dur-slide) var(--ease-out); }
.bigstat b .dc.on { color: var(--muted); }

/* Header backdrop: Canvas UI's Grid effect (desktop with a mouse only). */
.hero { position: relative; isolation: isolate; }
.hero .grid-src { display: none; }
.hero .grid-fx { display: none; }
@media (prefers-color-scheme: dark) { :root:not([data-theme="light"]) { --grid-alpha: .4; } }
:root[data-theme="dark"] { --grid-alpha: .4; }
@media (min-width: 901px) and (hover: hover) and (pointer: fine) and (prefers-reduced-motion: no-preference) {
  .hero { margin: -40px -16px 0 -32px; padding: 40px 16px 28px 32px; }
  .hero .grid-fx { display: block; position: absolute; inset: 0; width: 100%; height: 100%; z-index: -1; pointer-events: none; opacity: var(--grid-alpha, .32);
    -webkit-mask-image: linear-gradient(to bottom, #000 55%, transparent); mask-image: linear-gradient(to bottom, #000 55%, transparent); }
}
"""


def chips(names) -> str:
    return "<div class='chips'>" + "".join(f"<span class='chip'>{esc(n)}</span>" for n in names) + "</div>" if names else ""


class QuotePicker:
    """One real, verified quote per section, never the same quote twice on the page."""
    def __init__(self):
        self.used = set()

    def pick(self, ids, ctx) -> str:
        cands = []
        for i in ids:
            r = ctx.rows.get(i)
            if not r or i not in ctx.allowed or r["quote_verified"] != "True":
                continue
            q = r["short_quote"].strip()
            n = len(q.split())
            if n < 8 or q in self.used:
                continue
            cands.append((bool(r["who"]), -abs(n - 16), r))
        if not cands:
            return ""
        _, _, r = max(cands, key=lambda c: (c[0], c[1]))
        self.used.add(r["short_quote"].strip())
        who = f"{esc(r['who'])}, " if r["who"] else ""
        return (f"<figure class='pq'><blockquote>“{esc(r['short_quote'].strip())}”</blockquote>"
                f"<figcaption>{who}<a href='{esc(r['url'])}' target='_blank' rel='noopener'>{esc(r['source'])}, "
                f"{esc(short_date(r['date']))}</a></figcaption></figure>")


def kp_v2(reply, ctx) -> str:
    cards = "".join(f"<div class='card'><span class='num'>{n:02d}</span><h4>{inline(k['headline'])}</h4>"
                    f"<p>{inline(k['detail'])}</p>{ctx.src(k['evidence_ids'])}</div>"
                    for n, k in enumerate(reply["key_points"], 1))
    return f"<section class='s' aria-label='Key points'><div class='kp2'>{cards}</div></section>"


PAGE_QUOTES = [None]  # one QuotePicker per page build, shared by all tabs


def nice_window(w: str) -> str:
    """'2025-11-11 to 2026-11-14' -> '11 Nov 2025 to 14 Nov 2026'."""
    def d(x):
        y, m, dd = x.split("-")
        return f"{int(dd)} {MONTHS[int(m) - 1]} {y}"
    parts = re.findall(r"\d{4}-\d{2}-\d{2}", w)
    return " to ".join(d(x) for x in parts) if len(parts) == 2 else esc(w)


def intro(p) -> str:
    """What the page is, how it was made, how to read it. Facts come from the pack."""
    o = p["overview"]
    return (
        "<section class='intro' aria-label='About this page'><h3>What this page is</h3>"
        f"<p class='lead'>A year of public AI commentary ({nice_window(o['window'])}) boiled down into four short reports. "
        f"It draws on {o['items']:,} articles, newsletter issues, forum threads and posts from {len(o['sources'])} sources, "
        f"broken into {o['findings']:,} <i>findings</i>: single points someone made, such as a complaint, a tool tip or one "
        "side of an argument.</p><ul>"
        "<li><b>How it was made.</b> AI models (Claude) pulled out the findings, grouped them into themes and wrote these "
        "summaries. Every count and chart is computed by code, every quote is real, and every card links to its sources.</li>"
        "<li><b>Where it comes from.</b> Tech newsletters and blogs, the Hacker News forum and selected Bluesky accounts. "
        "They lean toward developers and AI insiders, so this shows what that crowd talked about, not what everyone thinks.</li>"
        "<li><b>Reading the numbers.</b> <b>x2.4</b> means a topic took up 2.4 times as big a share of the conversation in "
        "Jul to Oct 2026 as in Dec 2025 to Mar 2026 (a small cushion stops topics that start near zero from showing absurd "
        "jumps). <b>Rising</b> or <b>falling</b> means most of the six biggest sources agree, not just one.</li>"
        "<li><b>Two kinds of reader.</b> Sections marked <span class='aud'>For builders</span> are for people who build "
        "with AI coding tools; they start folded.</li></ul>"
        "<p class='start'>New to this? Start with <a href='#debates'>Debates</a>, then <i>What this means for you</i> below, "
        "then the first sections of <a href='#tools'>Tools</a>.</p></section>")


AUD = "<span class='aud'>For builders</span>"
CHEV = ('<svg class="chev" viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="2" '
        'stroke-linecap="round" stroke-linejoin="round"><path d="M6 9l6 6 6-6"/></svg>')


def foldable(head_html: str, body_html: str, open_: bool = True) -> str:
    """A section whose heading row (title, takeaway, big number) folds the cards beneath it."""
    return (f"<section class='s'><details class='fold'{' open' if open_ else ''}><summary>{head_html}</summary>"
            f"<div class='fold-body'>{body_html}</div></details></section>")


BUILDER = re.compile(r"\bbuilders?\b|building with|coding|builds work|developer", re.I)


def sec_head(s, builder=False) -> str:
    stat = (f"<div class='bigstat'><b>{esc(s['stat_value'])}</b><span>{esc(s['stat_label'])}</span></div>"
            if s.get("stat_value") else "")
    return (f"<div class='sec-head'><div class='sec-title'><h3>{icon(icon_for(s['heading']))}{inline(s['heading'])}{AUD if builder else ''}{CHEV}</h3>"
            f"<p class='takeaway'>{inline(s['takeaway'])}</p></div>{stat}</div>")


def card_v2(c, ctx, with_icon=True) -> str:
    ic = icon(icon_for(c["label"] + " " + c["text"])) if with_icon else ""
    return (f"<div class='card'><div class='ch'>{ic}<h4>{inline(c['label'])}</h4></div>{chips(c['people'])}"
            f"<p>{inline(c['text'])}</p>{ctx.src(c['evidence_ids'])}</div>")


def section_v2(s, ctx, quotes, fold=False, auto=True) -> str:
    cards = s["cards"]
    builder = s.get("audience") == "builders" if s.get("audience") else bool(BUILDER.search(s["heading"]))
    numbered = cards and all(re.match(r"^\d+\.", c["label"]) for c in cards)
    if numbered:
        body = "<div class='steps'>" + "".join(
            f"<div class='step'><span class='badge'>{esc(re.match(r'^(\d+)', c['label']).group(1))}</span><div>"
            f"<h4>{inline(re.sub(r'^\d+\.\s*', '', c['label']))}</h4>{chips(c['people'])}<p>{inline(c['text'])}</p>"
            f"{ctx.src(c['evidence_ids'])}</div></div>" for c in cards) + "</div>"
    else:
        body = f"<div class='cards'>{''.join(card_v2(c, ctx) for c in cards)}</div>"
    post = ""  # post angles live in post_ideas.md, not on the page (owner, 2026-11-22)
    q = quotes.pick([i for c in cards for i in c["evidence_ids"]], ctx)
    return foldable(sec_head(s, builder), f"{body}{q}{post}", open_=not (fold or (builder and auto)))


def year_strip(moments, p, ctx) -> str:
    months = list(p["trends"]["terms"][0]["monthly_per_1k"]) if p["trends"]["terms"] else []
    if not months:
        return ""
    if not moments:  # fallback: spike terms
        moments = [{"month": s["month"], "label": f"{s['term']} spike", "evidence_ids": []} for s in p["spikes"]]
    by = {}
    for m in moments:
        by.setdefault(m["month"], []).append(m)
    while len(months) > 1 and months[-1] not in by:  # e.g. a partial last month: more room for the labels
        months.pop()
    cols = "".join(
        f"<div class='year-col'><span class='mo'>{MONTHS[int(mo[5:]) - 1]} {mo[2:4]}</span>"
        + "".join(f"<div class='moment'>{inline(m['label'])}</div>" for m in by.get(mo, [])) + "</div>"
        for mo in months)
    return (f"<div class='chart'><h4>{icon('bolt')} The year in AI</h4><p class='note'>Key moments, from the months when a "
            f"topic spiked far above its usual level.</p><div class='year' lang='en'><div class='year-grid' style='--cols:{len(months)}'>"
            f"{cols}</div></div></div>")


def heatmap(p) -> str:
    doms = sorted(p["trends"]["domains"], key=lambda x: -x["ratio"])
    if not doms:
        return ""
    months = list(doms[0]["monthly_per_1k"])
    head = "<span></span>" + "".join(f"<span class='hd'>{MONTHS[int(m[5:]) - 1][:1]}<br>{m[2:4]}</span>" for m in months) + "<span></span>"
    rows = ""
    for d in doms:
        vals = [d["monthly_per_1k"][m] for m in months]
        lo, hi = min(vals), max(vals)
        span = (hi - lo) or 1
        cells = "".join(f"<span class='heat-cell' title='{esc(d['key'])}, {m}: {v:.0f} per 1,000 findings'>"
                        f"<i style='opacity:{0.06 + 0.94 * (v - lo) / span:.2f}'></i></span>" for m, v in zip(months, vals))
        rows += f"<span>{esc(d['key'])}</span>{cells}<span class='pill {d['verdict']}'>{d['verdict']}</span>"
    return (f"<div class='chart'><h4>{icon('chart')} Where attention went, month by month</h4><p class='note'>Each row is a "
            "topic area; darker = a bigger share of that month's findings, from the row's own lowest month (pale) to its highest (dark). Sorted by overall change; the label says "
            "whether most big sources agreed. These are broad topic groups, so a group can stay flat while one keyword "
            f"inside it (such as 'open weights') rises.</p><div class='heat'><div class='heat-grid' style='--cols:{len(months)}'>"
            f"{head}{rows}</div></div></div>")


def bubble_chart(p, n=60, labels=10) -> str:
    g = [x for x in p.get("theme_growth", []) if x["findings"] >= 30][:n]
    if len(g) < 5:
        return ""
    W, H, L, R, T, B = 720, 420, 48, 20, 24, 40
    fx = [math.log10(x["findings"]) for x in g]
    fy = [max(-3, min(3, math.log2(x["ratio"]))) for x in g]
    x0, x1 = min(fx), max(fx)
    sx = lambda v: L + (v - x0) / ((x1 - x0) or 1) * (W - L - R)
    sy = lambda v: T + (3 - v) / 6 * (H - T - B)
    xmid = sorted(fx)[len(fx) // 2]
    out = [f'<line x1="{sx(xmid):.0f}" y1="{T}" x2="{sx(xmid):.0f}" y2="{H - B}"/>',
           f'<line x1="{L}" y1="{sy(0):.0f}" x2="{W - R}" y2="{sy(0):.0f}"/>',
           f'<text class="q" x="{W - R - 4}" y="{T + 12}" text-anchor="end">big &amp; growing</text>',
           f'<text class="q" x="{L + 4}" y="{T + 12}">niche &amp; growing</text>',
           f'<text class="q" x="{W - R - 4}" y="{H - B - 8}" text-anchor="end">big &amp; fading</text>',
           f'<text class="q" x="{L + 4}" y="{H - B - 8}">niche &amp; fading</text>',
           f'<text class="ax" x="{(L + W - R) / 2:.0f}" y="{H - 10}" text-anchor="middle">size: findings (log scale) →</text>',
           f'<text class="ax" x="14" y="{(T + H - B) / 2:.0f}" text-anchor="middle" transform="rotate(-90 14 {(T + H - B) / 2:.0f})">growth: late vs early share →</text>']
    order = sorted(range(len(g)), key=lambda i: -g[i]["findings"])
    # Label the most notable themes (biggest, and biggest movers), skipping any label that would overlap another
    # label or a corner caption. Every dot still has a hover title.
    priority = sorted(range(len(g)), key=lambda i: -(fx[i] - x0 + 0.6) * (abs(fy[i]) + 0.4))
    boxes = [(L, T, L + 150, T + 16), (W - R - 150, T, W - R, T + 16),
             (L, H - B - 22, L + 150, H - B), (W - R - 150, H - B - 22, W - R, H - B)]
    placed = []
    for i in priority:
        if len(placed) >= labels:
            break
        t = g[i]["title"]
        t = t if len(t) <= 34 else t[:32].rsplit(" ", 1)[0] + "…"
        cx, cy = sx(fx[i]), sy(fy[i])
        w = 6.0 * len(t)
        right = cx + 8 + w <= W - R
        bx = (cx + 8, cy - 7, cx + 8 + w, cy + 6) if right else (cx - 8 - w, cy - 7, cx - 8, cy + 6)
        if bx[0] < L or any(not (bx[2] < b[0] or bx[0] > b[2] or bx[3] < b[1] or bx[1] > b[3]) for b in boxes):
            continue
        boxes.append(bx)
        placed.append((i, t, bx[0] if right else bx[2], "start" if right else "end", cy))
    for i in order:
        x = g[i]
        cls = "up" if x["ratio"] >= 1.5 else "down" if x["ratio"] <= 0.67 else "flat"
        r = 3 + 1.4 * math.sqrt(x["n_sources"])
        tip = f"{x['title']} ({x['domain']}): {x['findings']} findings, {x['n_sources']} sources, ×{x['ratio']} late vs early"
        out.append(f'<circle class="{cls}" cx="{sx(fx[i]):.1f}" cy="{sy(fy[i]):.1f}" r="{r:.1f}"><title>{esc(tip)}</title></circle>')
    for i, t, tx, anchor, cy in placed:
        out.append(f'<text x="{tx:.0f}" y="{cy + 4:.0f}" text-anchor="{anchor}">{esc(t)}</text>')
    return (f"<div class='chart'><h4>{icon('bolt')} What's big, and what's growing</h4><p class='note'>Each dot is a theme with "
            "30+ findings. Right = more findings; up = a bigger share of the conversation late in the year than early. "
            "Dot size = number of sources. Hover a dot for its name.</p>"
            f'<div class="bubwrap"><svg class="bubbles" viewBox="0 0 {W} {H}" role="img" aria-label="Themes by size and growth">{"".join(out)}</svg></div></div>')


def voices_map(positions) -> str:
    if not positions:
        return ""
    grid = {}
    for v in positions:
        grid.setdefault((v["builder_commentator"], v["skeptic_enthusiast"]), []).append(v)
    rows = ""
    for y in (2, 1, 0, -1, -2):  # top = enthusiast
        yl = {2: "enthusiast", 0: "", -2: "skeptic"}.get(y, "")
        rows += f"<span class='yl'>{yl}</span>" if yl else "<span></span>"
        for x in (-2, -1, 0, 1, 2):
            names = "".join(f"<span class='vname' title='{esc(v['one_line'])}'>{esc(v['name'])}</span>" for v in grid.get((x, y), []))
            rows += f"<div class='cell{' mid' if x == 0 or y == 0 else ''}'>{names}</div>"
    return (f"<div class='chart'><h4>{icon('people')} Where they stand</h4><p class='note'>Sonnet's reading of each "
            "person's findings, not their own labels. Hover a name for a one-line summary.</p>"
            f"<div class='vmap'>{rows}<span></span><div class='xl'><span>hands-on builder</span><span>commentator</span></div></div></div>")


def header_v2(eyebrow, reply, p) -> str:
    o = p["overview"]
    return (f"<div class='hero'><canvas class='grid-src'></canvas><canvas class='grid-fx' aria-hidden='true'></canvas>"
            f"<header><div class='eyebrow'>{esc(eyebrow)}</div><h2>{inline(reply['title'])}</h2>"
            f"<p class='dek'>{inline(reply['dek'])}</p><div class='meta'>{esc(o['window'])} · {o['findings']:,} findings · "
            f"{len(o['sources'])} sources</div><div class='foldbar'><button type='button' data-fold='open'>Expand all</button>"
            f"<button type='button' data-fold='close'>Collapse all</button></div></header></div>")


def state_v2(reply, ctx) -> str:
    p, q = ctx.p, PAGE_QUOTES[0]
    out = [header_v2("State of AI", reply, p), intro(p), kp_v2(reply, ctx), year_strip(reply.get("moments"), p, ctx)]
    secs, i = reply["sections"], 0
    while i < len(secs):
        s, h = secs[i], secs[i]["heading"].lower()
        if "struggl" in h and i + 1 < len(secs) and "struggl" in secs[i + 1]["heading"].lower():
            out.append(f"<div class='split'><div>{section_v2(s, ctx, q, auto=False)}</div><div>{section_v2(secs[i + 1], ctx, q, auto=False)}</div></div>")
            i += 2
            continue
        out.append(section_v2(s, ctx, q, fold=bool(FOLD.search(h))))
        i += 1
    return "".join(out)


def debates_v2(reply, ctx) -> str:
    p, q = ctx.p, PAGE_QUOTES[0]
    out = [header_v2("Debates", reply, p), kp_v2(reply, ctx), debate_chart(p)]
    for n, s in enumerate(reply["sections"], 1):
        cards = s["cards"]
        sides, rest = cards[:2], cards[2:]
        html_ = (f"<details class='debate2 fold'{' open' if n == 1 else ''}><summary><span class='kicker'>Debate {n}</span>"
                 f"<h4>{icon(icon_for(s['heading'] + ' ' + s['takeaway']))}{inline(s['heading'])}{CHEV}</h4>"
                 f"<p class='q'>{inline(s['takeaway'])}</p></summary><div class='fold-body'>")
        if len(sides) == 2:
            a, b = sides
            html_ += ("<div class='vs'>" + "".join(
                f"<div class='sidebox {cls}'><h5>{inline(c['label'])}</h5>{chips(c['people'])}<p>{inline(c['text'])}</p>{ctx.src(c['evidence_ids'])}</div>"
                + ("<span class='v'>vs</span>" if cls == "a" else "") for cls, c in (("a", a), ("b", b))) + "</div>")
        else:
            rest = cards
        if rest:
            html_ += "<div class='extra'>" + "".join(
                f"<div><span class='kicker'>{inline(c['label'])}</span>{chips(c['people'])}<p>{inline(c['text'])}</p>{ctx.src(c['evidence_ids'])}</div>"
                for c in rest) + "</div>"
        html_ += q.pick([i for c in cards for i in c["evidence_ids"]], ctx)
        out.append(html_ + "</div></details>")
    return "".join(out)


def trends_v2(reply, ctx) -> str:
    p, q, tr = ctx.p, PAGE_QUOTES[0], ctx.p["trends"]
    out = [header_v2("Trends", reply, p), kp_v2(reply, ctx), change_chart(p, 16), heatmap(p), bubble_chart(p)]
    out += [section_v2(s, ctx, q, fold=bool(FOLD.search(s["heading"]))) for s in reply["sections"]]
    out.append(multiples(p))
    out.append("<details class='more'><summary>All the trend data</summary>"
               f"<p class='lede'>Periods: {esc(p['overview']['trend_periods'])}. Rising or falling = a change of 15% or more that "
               "at least four of the six biggest sources show on their own, with at most one against.</p>"
               "<h4>Domains</h4>" + trend_table(tr["domains"]) + "<h4>Finding types</h4>" + trend_table(tr["types"])
               + "<h4>Terms (50+ findings, keyword matches)</h4>" + trend_table([x for x in tr["terms"] if x["findings"] >= 50])
               + "</details>")
    return "".join(out)


def tools_v2(reply, ctx) -> str:
    q = PAGE_QUOTES[0]
    out = [header_v2("Tools", reply, ctx.p), kp_v2(reply, ctx), tool_chart(ctx.p)]
    out += [section_v2(s, ctx, q, fold=bool(FOLD.search(s["heading"]))) for s in reply["sections"]]
    return "".join(out)


def voices_v2(reply, ctx) -> str:
    p, q = ctx.p, QuotePicker()
    by_name = {v["who"]: v for v in p["voices"]}
    top = max((v["findings"] for v in p["voices"]), default=1)
    out = [header_v2("Voices", reply, p), kp_v2(reply, ctx), voices_map(reply.get("voice_positions")), voice_chart(p, 15)]
    for s in reply["sections"]:
        cards = ""
        for c in s["cards"]:
            v = next((by_name[n] for n in c["people"] + [c["label"]] if n in by_name), None)
            stats = ""
            if v:
                stats = (f"<div class='person'><div class='stats'><span class='count'>{v['findings']:,} findings</span>"
                         + "".join(f"<span class='tag'>{esc(d)}</span>" for d in v["top_domains"][:2])
                         + f"</div><div class='meter'><span style='width:{100 * v['findings'] / top:.0f}%'></span></div></div>")
            cards += f"<div class='card'><h4>{inline(c['label'])}</h4>{stats}<p>{inline(c['text'])}</p>{ctx.src(c['evidence_ids'])}</div>"
        qt = q.pick([i for c in s["cards"] for i in c["evidence_ids"]], ctx)
        out.append(foldable(sec_head(s), f"<div class='cards'>{cards}</div>{qt}"))
    return "".join(out)


RENDERERS_V2 = {"state_of_ai": state_v2, "debates": debates_v2, "trends": trends_v2, "tools_guide": tools_v2, "voices": voices_v2}
