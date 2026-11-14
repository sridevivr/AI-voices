"""Render the insight reports as one self-contained web page: data/out/insights/site/index.html.

Called by `python -m src.insights site` (free: reads pack.json + replies.json, no API calls).
The page has one view per report (hash routes #state, #debates, #trends, #tools, #voices, #numbers),
source links on every cited paragraph, verdict pills and month-by-month sparklines for trends.
It follows the claude.ai Artifact page contract (no <html>/<head>/<body> tags; title + style first),
so it can be published as an Artifact as-is, and it also opens fine as a local file.
"""
from __future__ import annotations

import html
import json
import re

from .config import now_utc

VIEWS = [  # (hash, nav label, report name or None for the numbers view)
    ("state", "State of AI", "state_of_ai"),
    ("debates", "Debates", "debates"),
    ("trends", "Trends", "trends"),
    ("tools", "Tools", "tools_guide"),
    ("voices", "Voices", "voices"),
    ("numbers", "The numbers", None),
]

CSS = """
/* Layout: sticky left index of reports beside one ~68ch reading column; on phones the index becomes a
   sticky scrolling tab bar. Each report is a view; data (pills, sparklines, bars) uses the mono face. */
:root {
  --bg: #f5f7f9; --surface: #ffffff; --fg: #141a21; --muted: #586474; --line: #dce2e8;
  --accent: #0e6b63; --accent-soft: #e2f1ef;
  --up: #1d7a3c; --up-soft: #e3f3e8; --down: #b2442c; --down-soft: #f8e7e2; --mixed: #86691a; --mixed-soft: #f5efdc;
  --display: "Bricolage Grotesque", "Space Grotesk", system-ui, sans-serif;
  --body: "Inter", system-ui, -apple-system, "Segoe UI", sans-serif;
  --mono: "JetBrains Mono", ui-monospace, "SF Mono", Menlo, monospace;
}
@media (prefers-color-scheme: dark) { :root:not([data-theme="light"]) {
  --bg: #0e1215; --surface: #151b20; --fg: #e6eaee; --muted: #98a3af; --line: #26303a;
  --accent: #52c3b5; --accent-soft: #15302d;
  --up: #63c584; --up-soft: #163122; --down: #f08e76; --down-soft: #3a1e18; --mixed: #dbb64e; --mixed-soft: #332a12;
  color-scheme: dark; } }
:root[data-theme="dark"] {
  --bg: #0e1215; --surface: #151b20; --fg: #e6eaee; --muted: #98a3af; --line: #26303a;
  --accent: #52c3b5; --accent-soft: #15302d;
  --up: #63c584; --up-soft: #163122; --down: #f08e76; --down-soft: #3a1e18; --mixed: #dbb64e; --mixed-soft: #332a12;
  color-scheme: dark; }
* { box-sizing: border-box; }
body { background: var(--bg); color: var(--fg); font: 16px/1.6 var(--body); }
a { color: var(--accent); }
a:focus-visible, button:focus-visible { outline: 2px solid var(--accent); outline-offset: 2px; border-radius: 4px; }
.shell { display: grid; grid-template-columns: 240px minmax(0, 1fr); gap: 48px; max-width: 1160px; margin: 0 auto;
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
.view { display: grid; gap: 28px; max-width: 72ch; }
.view.wide { max-width: none; }
.eyebrow { font: 600 12px/1 var(--mono); text-transform: uppercase; letter-spacing: 0.08em; color: var(--accent); }
.view > header { display: grid; gap: 12px; }
.view h2 { font: 700 clamp(28px, 4vw, 40px)/1.1 var(--display); margin: 0; text-wrap: balance; letter-spacing: -0.015em; }
.dek { font-size: 19px; line-height: 1.5; color: var(--muted); margin: 0; }
.meta { font: 12px/1.5 var(--mono); color: var(--muted); }
.keypoints { background: var(--surface); border: 1px solid var(--line); border-radius: 12px; padding: 20px 24px; display: grid; gap: 12px; }
.keypoints h3 { margin: 0; font: 600 13px/1 var(--mono); text-transform: uppercase; letter-spacing: 0.08em; color: var(--muted); }
.keypoints ul { margin: 0; padding-left: 20px; display: grid; gap: 10px; }
section.s { display: grid; gap: 14px; }
section.s h3 { font: 650 22px/1.25 var(--display); margin: 8px 0 0; text-wrap: balance; }
section.s p, section.s li { margin: 0; }
section.s ul, section.s ol { margin: 0; padding-left: 22px; display: grid; gap: 6px; }
.cites { display: inline-flex; flex-wrap: wrap; gap: 6px; margin-left: 4px; vertical-align: 1px; }
.cite { font: 11px/1.6 var(--mono); padding: 0 7px; border-radius: 999px; border: 1px solid var(--line); color: var(--muted);
  text-decoration: none; white-space: nowrap; background: var(--surface); }
.cite:hover { color: var(--accent); border-color: var(--accent); }
.tablewrap { overflow-x: auto; border: 1px solid var(--line); border-radius: 12px; background: var(--surface); }
table { border-collapse: collapse; width: 100%; font-size: 14px; }
th, td { text-align: left; padding: 9px 14px; border-bottom: 1px solid var(--line); vertical-align: middle; }
th { font: 600 11px/1.3 var(--mono); text-transform: uppercase; letter-spacing: 0.06em; color: var(--muted); white-space: nowrap; }
tr:last-child td { border-bottom: 0; }
td.num { font: 13px/1.4 var(--mono); font-variant-numeric: tabular-nums; text-align: right; white-space: nowrap; }
.pill { font: 600 11px/1 var(--mono); padding: 4px 8px; border-radius: 999px; text-transform: uppercase; letter-spacing: 0.05em; white-space: nowrap; }
.pill.rising { color: var(--up); background: var(--up-soft); }
.pill.falling { color: var(--down); background: var(--down-soft); }
.pill.mixed { color: var(--mixed); background: var(--mixed-soft); }
.pill.flat { color: var(--muted); background: var(--bg); }
svg.spark { display: block; width: 120px; height: 28px; overflow: visible; }
svg.spark polyline { fill: none; stroke: var(--accent); stroke-width: 1.6; }
svg.spark circle { fill: var(--accent); }
svg.spark line { stroke: var(--line); stroke-width: 1; }
.bars { display: grid; gap: 6px; }
.bar { display: grid; grid-template-columns: 150px minmax(0, 1fr) 56px; gap: 12px; align-items: center; font-size: 14px; }
.bar .track { height: 10px; background: var(--line); border-radius: 999px; overflow: hidden; }
.bar .fill { height: 100%; background: var(--accent); border-radius: 999px; }
.bar .v { font: 13px/1 var(--mono); text-align: right; font-variant-numeric: tabular-nums; color: var(--muted); }
.tiles { display: grid; grid-template-columns: repeat(auto-fit, minmax(150px, 1fr)); gap: 12px; }
.tile { background: var(--surface); border: 1px solid var(--line); border-radius: 12px; padding: 16px; display: grid; gap: 4px; }
.tile b { font: 650 26px/1.1 var(--display); font-variant-numeric: tabular-nums; }
.tile span { font-size: 13px; color: var(--muted); }
.note { font-size: 14px; color: var(--muted); }
footer.f { margin-top: 48px; padding-top: 20px; border-top: 1px solid var(--line); font-size: 13px; color: var(--muted); max-width: 72ch; display: grid; gap: 8px; }
@media (max-width: 860px) {
  .shell { grid-template-columns: minmax(0, 1fr); gap: 20px; padding-block: 16px 48px; }
  .side { position: static; gap: 14px; }
  .nav { position: sticky; top: env(safe-area-inset-top, 0px); z-index: 5; display: flex; overflow-x: auto; gap: 4px;
    background: var(--bg); padding-block: 8px; border-bottom: 1px solid var(--line); }
  .nav a { white-space: nowrap; }
  .nav .n { display: none; }
  .facts { display: none; }
  .bar { grid-template-columns: 110px minmax(0, 1fr) 48px; }
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


def inline(s: str) -> str:
    s = esc(s)
    s = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", s)
    s = re.sub(r"(?<![\w*])\*(?!\s)(.+?)(?<!\s)\*(?![\w*])", r"<em>\1</em>", s)
    s = re.sub(r"`([^`]+)`", r"<code>\1</code>", s)
    return s


def short_date(d: str) -> str:
    months = "Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec".split()
    try:
        y, m, dd = d.split("-")
        return f"{months[int(m) - 1]} {int(dd)}, {y}"
    except (ValueError, IndexError):
        return d


def cites_html(ids, allowed, rows_by_fid) -> str:
    seen, out = set(), []
    for i in ids:
        r = rows_by_fid.get(i)
        if i not in allowed or not r or r["url"] in seen:
            continue
        seen.add(r["url"])
        out.append(f'<a class="cite" href="{esc(r["url"])}" target="_blank" rel="noopener" '
                   f'title="{esc(r["summary"])}">{esc(r["source"])} · {esc(short_date(r["date"]))}</a>')
    return f' <span class="cites">{"".join(out)}</span>' if out else ""


def para_html(text: str, cites: str) -> str:
    """A paragraph that may contain a Markdown list."""
    lines = [l for l in text.split("\n") if l.strip()]
    items = [l for l in lines if re.match(r"^\s*(?:[-*]|\d+\.)\s+", l)]
    if items and len(items) == len(lines):
        tag = "ol" if re.match(r"^\s*\d+\.", items[0]) else "ul"
        lis = "".join(f"<li>{inline(re.sub(r'^\s*(?:[-*]|\d+\.)\s+', '', l))}</li>" for l in items)
        return f"<{tag}>{lis}</{tag}>{('<p>' + cites + '</p>') if cites else ''}"
    return f"<p>{inline(' '.join(lines))}{cites}</p>"


def sparkline(series: dict) -> str:
    vals = list(series.values())
    if not vals:
        return ""
    w, h, top = 120, 28, max(vals) or 1
    pts = [(round(i * w / max(len(vals) - 1, 1), 1), round(h - 2 - (v / top) * (h - 6), 1)) for i, v in enumerate(vals)]
    months = list(series)
    label = f"{months[0]} to {months[-1]}: " + ", ".join(f"{v:.0f}" for v in vals) + " per 1,000 findings"
    x, y = pts[-1]
    return (f'<svg class="spark" viewBox="0 0 {w} {h}" role="img" aria-label="{esc(label)}"><title>{esc(label)}</title>'
            f'<line x1="0" y1="{h - 2}" x2="{w}" y2="{h - 2}"/>'
            f'<polyline points="{" ".join(f"{a},{b}" for a, b in pts)}"/><circle cx="{x}" cy="{y}" r="2.5"/></svg>')


def trend_rows(items, spark=True) -> str:
    rows = []
    for x in items:
        rows.append(f"<tr><td>{esc(x['key'])}</td><td class='num'>{x['findings']:,}</td>"
                    f"<td class='num'>{x['early_per_1k']} → {x['late_per_1k']}</td><td class='num'>×{x['ratio']}</td>"
                    f"<td class='num'>{x['big_sources_up']} / {x['big_sources_down']}</td>"
                    f"<td><span class='pill {x['verdict']}'>{x['verdict']}</span></td>"
                    + (f"<td>{sparkline(x['monthly_per_1k'])}</td>" if spark else "") + "</tr>")
    head = ("<tr><th>Topic</th><th>Findings</th><th>Early → late (per 1k)</th><th>Change</th>"
            "<th>Big sources ↑ / ↓</th><th>Verdict</th>" + ("<th>By month</th>" if spark else "") + "</tr>")
    return f"<div class='tablewrap'><table><thead>{head}</thead><tbody>{''.join(rows)}</tbody></table></div>"


def voices_table(p) -> str:
    rows = "".join(f"<tr><td>{esc(v['who'])}</td><td class='num'>{v['findings']:,}</td>"
                   f"<td>{esc(', '.join(v['top_domains']))}</td><td>{esc(', '.join(v['via']))}</td></tr>"
                   for v in p["voices"])
    return ("<section class='s'><h3>Who drives the conversation</h3><div class='tablewrap'><table><thead><tr><th>Person</th>"
            f"<th>Findings</th><th>Mostly about</th><th>Via</th></tr></thead><tbody>{rows}</tbody></table></div>"
            "<p class='note'>Counts reflect how much each source publishes and quotes, not influence.</p></section>")


def tool_bars(p, k=20) -> str:
    items = list(p["tools"]["counts"].items())[:k]
    top = items[0][1] if items else 1
    bars = "".join(f"<div class='bar'><span>{esc(n)}</span><div class='track'><div class='fill' style='width:{100 * v / top:.1f}%'></div></div>"
                   f"<span class='v'>{v:,}</span></div>" for n, v in items)
    return ("<section class='s'><h3>Most-mentioned tools</h3><p class='note'>Mentions in tool, technique and workaround "
            "findings. These sources lean toward builders and toward Claude, so read this as what this crowd recommends, "
            f"not market share.</p><div class='bars'>{bars}</div></section>")


def trend_tables(p) -> str:
    tr = p["trends"]
    period = p["overview"]["trend_periods"]
    monthly = [x for x in tr["terms"] if x["findings"] >= 50]
    return (f"<section class='s'><h3>Domains</h3><p class='note'>Periods: {esc(period)}. "
            "<strong>Rising</strong> or <strong>falling</strong> means a change of 15% or more that at least four of the six "
            "biggest sources show on their own, with at most one against.</p>" + trend_rows(tr["domains"]) + "</section>"
            "<section class='s'><h3>Finding types</h3>" + trend_rows(tr["types"]) + "</section>"
            "<section class='s'><h3>Terms</h3><p class='note'>Keyword matches in each finding's summary and quote "
            "(50+ findings), so approximate.</p>" + trend_rows(monthly) + "</section>")


def report_view(p, name, reply, rows_by_fid, from_insights) -> str:
    allowed = set(reply.get("_allowed") or from_insights.allowed_ids(p, name))
    kp = "".join(f"<li>{inline(k['text'])}{cites_html(k['evidence_ids'], allowed, rows_by_fid)}</li>"
                 for k in reply["key_points"])
    secs = "".join(
        f"<section class='s'><h3>{inline(s['heading'])}</h3>"
        + "".join(para_html(pp["text"], cites_html(pp["evidence_ids"], allowed, rows_by_fid)) for pp in s["paragraphs"])
        + "</section>" for s in reply["sections"])
    extra = ""
    for tb in from_insights.REPORTS[name]["tables"]:
        extra += {"voices": voices_table(p), "tool_counts": tool_bars(p), "trend_tables": trend_tables(p)}.get(tb, "")
    o = p["overview"]
    return (f"<header><div class='eyebrow'>{esc(dict((v[2], v[1]) for v in VIEWS)[name])}</div>"
            f"<h2>{inline(reply['title'])}</h2><p class='dek'>{inline(reply['dek'])}</p>"
            f"<div class='meta'>{esc(o['window'])} · {o['findings']:,} findings · {len(o['sources'])} sources</div></header>"
            f"<div class='keypoints'><h3>Key points</h3><ul>{kp}</ul></div>{secs}{extra}")


def numbers_view(p, rows_by_fid) -> str:
    o, tr = p["overview"], p["trends"]
    t = o["types"]
    tiles = "".join(f"<div class='tile'><b>{v:,}</b><span>{esc(k.replace('_', ' '))}</span></div>" for k, v in t.items())
    first = lambda ev: rows_by_fid.get(int(ev.split()[0][1:]))
    deb = "".join(
        f"<tr><td>{esc(d['title'])}</td><td class='num'>{d['types'].get('debate', 0)}</td><td class='num'>{d['findings']}</td>"
        f"<td class='num'>{d['n_sources']}</td></tr>" for d in p["debates"])
    use = lambda g: "".join(
        f"<tr><td>{esc(x['title'])}</td><td class='num'>{x['types'].get('tool_or_technique', 0) + x['types'].get('workaround', 0)}</td>"
        f"<td class='num'>{x['n_sources']}</td><td>{esc(x['current_solutions'])}</td></tr>" for x in p["tools"][g][:10])
    sp = "".join(f"<tr><td>{esc(s['term'])}</td><td class='num'>{esc(s['month'])}</td><td class='num'>{s['peak_per_1k']}</td>"
                 f"<td class='num'>{s['median_per_1k']}</td></tr>" for s in p["spikes"])
    moved = [x for x in tr["domains"] + tr["terms"] if x["verdict"] in ("rising", "falling")]
    srcs = "".join(f"<tr><td>{esc(s)}</td><td class='num'>{n:,}</td></tr>" for s, n in o["sources"].items())
    return (f"<header><div class='eyebrow'>The numbers</div><h2>Every figure, computed from the findings</h2>"
            f"<p class='dek'>{o['findings']:,} findings from {o['items']:,} articles and threads by {len(o['sources'])} sources, "
            f"{esc(o['window'])}. {o['quotes_verified_pct']}% of quotes verified word-for-word against the source. "
            "No model wrote this page.</p></header>"
            f"<div class='tiles'>{tiles}</div>"
            "<section class='s'><h3>Biggest debates</h3><div class='tablewrap'><table><thead><tr><th>Debate</th><th>Debate findings</th>"
            f"<th>All findings</th><th>Sources</th></tr></thead><tbody>{deb}</tbody></table></div></section>"
            "<section class='s'><h3>What practitioners use: building with AI</h3><div class='tablewrap'><table><thead><tr><th>Theme</th>"
            f"<th>Tool + workaround findings</th><th>Sources</th><th>Named</th></tr></thead><tbody>{use('building')}</tbody></table></div></section>"
            "<section class='s'><h3>What practitioners use: everyday and business</h3><div class='tablewrap'><table><thead><tr><th>Theme</th>"
            f"<th>Tool + workaround findings</th><th>Sources</th><th>Named</th></tr></thead><tbody>{use('everyday')}</tbody></table></div></section>"
            + tool_bars(p)
            + "<section class='s'><h3>Confirmed trends</h3>" + trend_rows(moved) + "</section>"
            "<section class='s'><h3>Spikes</h3><p class='note'>One month far above the usual level: launches and viral moments.</p>"
            "<div class='tablewrap'><table><thead><tr><th>Term</th><th>Month</th><th>Peak per 1k</th><th>Median</th></tr></thead>"
            f"<tbody>{sp}</tbody></table></div></section>"
            + voices_table(p)
            + "<section class='s'><h3>Findings by source</h3><div class='tablewrap'><table><thead><tr><th>Source</th><th>Findings</th>"
            f"</tr></thead><tbody>{srcs}</tbody></table></div></section>")


def build_site(p: dict, replies: dict, rows_by_fid: dict, from_insights) -> str:
    o = p["overview"]
    views = [v for v in VIEWS if v[2] is None or v[2] in replies]
    nav = "".join(f"<a href='#{h}'><span>{esc(label)}</span><span class='n'>{n:02d}</span></a>"
                  for n, (h, label, _) in enumerate(views, 1))
    body = ""
    for h, label, name in views:
        inner = numbers_view(p, rows_by_fid) if name is None else report_view(p, name, replies[name], rows_by_fid, from_insights)
        wide = " wide" if name in (None, "trends") else ""
        body += f"<article class='view{wide}' id='v-{h}' aria-label='{esc(label)}'>{inner}</article>"
    facts = (f"<div class='facts'><div><b>{o['findings']:,}</b> findings</div><div><b>{len(o['sources'])}</b> sources</div>"
             f"<div><b>{o['items']:,}</b> articles &amp; threads</div><div>{esc(o['window'])}</div></div>")
    return f"""<title>AI Voices 2026</title>
<meta name="claude:viewport-fit-sides" content="cover">
<meta name="description" content="What a year of AI commentary says: debates, trends, tools and voices.">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,600;12..96,700&family=Inter:wght@400;500;600&family=JetBrains+Mono:wght@400;600&display=swap">
<style>{CSS}</style>
<div class="shell">
  <aside class="side">
    <div class="brand"><h1>AI Voices 2026</h1><p>What a year of AI commentary says, from {len(o['sources'])} newsletters, blogs and Hacker News.</p></div>
    <nav class="nav" aria-label="Reports">{nav}</nav>
    {facts}
  </aside>
  <main>
    {body}
    <footer class="f">
      <div>Generated {now_utc():%Y-%m-%d} by the AI Voices pipeline: articles fetched from {len(o['sources'])} public sources,
      findings extracted by Claude Haiku 5.5, grouped into themes and written up by Claude Sonnet 5.5. Every number and table is
      computed from the findings; every source link is a finding the text cites.</div>
      <div>Limits: the sources lean toward builders and AI insiders; mainstream business press, non-English sources and video are
      not included; paid Substack posts were skipped. Counts measure attention, not how many people experience something.</div>
    </footer>
  </main>
</div>
<script>{JS % json.dumps([v[0] for v in views])}</script>
"""
