"""Performance — the record so far, measured against the S&P 500.

Everything on this page computes from data/performance.csv. The CSV column is
still named `benchmark`; only the labels shown to a reader say S&P 500, so an
existing file keeps working.
"""

from pathlib import Path

import altair as alt
import pandas as pd
import streamlit as st

from lib.components import eyebrow, footer, heading, rule, section, stat
from lib.theme import FONTS, PALETTE

DATA = Path(__file__).resolve().parent.parent / "data" / "performance.csv"

CENTERED = (
    "line-height:1.7; max-width:62ch; margin:0 auto !important;"
    "text-align:center !important; color:var(--hx-bone);"
)

section()
eyebrow("Performance")

try:
    perf = pd.read_csv(DATA, parse_dates=["date"])
except FileNotFoundError:
    st.error(
        "No performance file found. Add one at data/performance.csv with "
        "columns: date, nav, benchmark."
    )
    st.stop()

# --- Summary statistics -----------------------------------------------------
# With fewer than two rows there is nothing to compute, so show an em-dash
# rather than nan. A dash reads as "not yet"; nan reads as broken.
enough = len(perf) >= 2


def pct(value: float, signed: bool = False) -> str:
    if not enough or pd.isna(value):
        return "—"
    return f"{value:+.1%}" if signed else f"{value:.1%}"


if enough:
    returns = perf["nav"].pct_change().dropna()
    total = perf["nav"].iloc[-1] / perf["nav"].iloc[0] - 1
    bench_total = perf["benchmark"].iloc[-1] / perf["benchmark"].iloc[0] - 1
    vol = returns.std() * (252 ** 0.5) if len(returns) > 1 else float("nan")
    peak = perf["nav"].cummax()
    max_dd = ((perf["nav"] - peak) / peak).min()
else:
    total = bench_total = vol = max_dd = float("nan")

c1, c2, c3, c4 = st.columns(4)
with c1:
    stat(pct(total, signed=True), "Total return")
with c2:
    stat(pct(total - bench_total, signed=True), "vs S&P 500")
with c3:
    stat(pct(vol), "Annualized vol")
with c4:
    stat(pct(max_dd), "Max drawdown")

rule()

# --- Chart ------------------------------------------------------------------
eyebrow("Growth of 100")
heading("Fund against the S&P 500")

tidy = perf.melt("date", ["nav", "benchmark"], var_name="series", value_name="value")
tidy["series"] = tidy["series"].map({"nav": "Haruspex", "benchmark": "S&P 500"})

chart = (
    alt.Chart(tidy)
    .mark_line(strokeWidth=1.8, point=len(perf) < 5)
    .encode(
        x=alt.X("date:T", title=None, axis=alt.Axis(grid=False)),
        y=alt.Y(
            "value:Q",
            title=None,
            scale=alt.Scale(zero=False),
            axis=alt.Axis(gridColor=PALETTE["line"], gridOpacity=0.6),
        ),
        color=alt.Color(
            "series:N",
            title=None,
            scale=alt.Scale(
                domain=["Haruspex", "S&P 500"],
                range=[PALETTE["bronze"], PALETTE["ash"]],
            ),
            legend=alt.Legend(orient="top-left", labelColor=PALETTE["bone"]),
        ),
        tooltip=["date:T", "series:N", alt.Tooltip("value:Q", format=".2f")],
    )
    .properties(height=340)
    .configure_view(strokeWidth=0)
    .configure_axis(
        labelColor=PALETTE["ash"],
        labelFont=FONTS["data"].split(",")[0].strip("'"),
        domainColor=PALETTE["line"],
        tickColor=PALETTE["line"],
    )
    .configure(background="transparent")
)
st.altair_chart(chart, width="stretch")

rule()

# --- The caveat -------------------------------------------------------------
eyebrow("Read this before the numbers")
st.markdown(
    f'<p style="{CENTERED}">'
    "This record is short. The fund started in August 2026, and a few weeks of "
    "numbers tell you close to nothing — a good stretch this early is as "
    "likely to be luck as skill. The leveraged positions also mean the swings "
    "are wider than the returns suggest, so the drawdown is the number worth "
    "watching, not the total. We publish from the beginning rather than "
    "waiting for a flattering run to start from."
    "</p>",
    unsafe_allow_html=True,
)

footer()
