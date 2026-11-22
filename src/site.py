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

from .config import now_utc

VIEWS = [  # (hash, nav label, report name)
    ("state", "State of AI", "state_of_ai"),
    ("debates", "Debates", "debates"),
    ("trends", "Trends", "trends"),
    ("tools", "Tools", "tools_guide"),
    ("voices", "Voices", "voices"),
]

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
    nav = "".join(f"<a href='#{h}'><span>{esc(label)}</span><span class='n'>{n:02d}</span></a>"
                  for n, (h, label, _) in enumerate(views, 1))
    body = ""
    for h, label, name in views:
        reply = replies[name]
        ctx = Ctx(p, rows_by_fid, set(reply.get("_allowed") or from_insights.allowed_ids(p, name)))
        body += f"<article class='view' id='v-{h}' aria-label='{esc(label)}'>{RENDERERS[name](reply, ctx)}</article>"
    kinds = "newsletters, blogs, Hacker News" + (" and Bluesky" if "Bluesky" in o["sources"] else "")
    facts = (f"<div class='facts'><div><b>{o['findings']:,}</b> findings</div><div><b>{len(o['sources'])}</b> sources</div>"
             f"<div><b>{o['items']:,}</b> articles, threads &amp; posts</div><div>{esc(o['window'])}</div></div>")
    return f"""<title>AI Voices 2026</title>
<meta name="claude:viewport-fit-sides" content="cover">
<meta name="description" content="What a year of AI commentary says: the state of AI, debates, trends, tools and voices.">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,600;12..96,700&family=Inter:wght@400;500;600&family=JetBrains+Mono:wght@400;600&display=swap">
<style>{CSS}</style>
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
    </footer>
  </main>
</div>
<script>{JS % json.dumps([v[0] for v in views])}</script>
"""
