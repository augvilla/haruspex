"""Performance — the record so far, measured against the S&P 500.

data/performance.csv holds CUMULATIVE PERCENTAGE GROWTH, not prices: the first
row is 0.0 and 0.10 means up ten percent since inception. Every figure is
derived by converting that to a growth index (1 + value) first, so a starting
value of zero never lands in a denominator.
"""

from pathlib import Path

import altair as alt
import pandas as pd
import streamlit as st

from lib.components import eyebrow, footer, heading, rule, section, stat
from lib.theme import FONTS, PALETTE

DATA = Path(__file__).resolve().parent.parent / "data" / "performance.csv"

section()
eyebrow("Performance")

try:
    perf = pd.read_csv(DATA, parse_dates=["date"]).sort_values("date")
except FileNotFoundError:
    st.error(
        "No performance file found. Add one at data/performance.csv with "
        "columns: date, nav, benchmark — both as cumulative growth, starting "
        "at 0."
    )
    st.stop()

enough = len(perf) >= 2

# Growth index: 0.10 becomes 1.10, so ratios and drawdowns behave normally.
nav_index = 1 + perf["nav"]
bench_index = 1 + perf["benchmark"]


def pct(value: float, signed: bool = False) -> str:
    """Format a rate, or an em-dash when there isn't enough data yet."""
    if not enough or value is None or pd.isna(value):
        return "—"
    return f"{value:+.1%}" if signed else f"{value:.1%}"


if enough:
    total = nav_index.iloc[-1] / nav_index.iloc[0] - 1
    bench_total = bench_index.iloc[-1] / bench_index.iloc[0] - 1
    daily = nav_index.pct_change().dropna()
    vol = daily.std() * (252 ** 0.5) if len(daily) > 1 else None
    peak = nav_index.cummax()
    max_dd = ((nav_index - peak) / peak).min()
else:
    total = bench_total = vol = max_dd = None

c1, c2, c3, c4 = st.columns(4)
with c1:
    stat(pct(total, signed=True), "Total return")
with c2:
    stat(
        pct(total - bench_total, signed=True) if enough else "—",
        "vs S&P 500",
    )
with c3:
    stat(pct(vol), "Annualized vol")
with c4:
    stat(pct(max_dd), "Max drawdown")

rule()

# --- Chart ------------------------------------------------------------------
eyebrow("Return since inception")
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
            # Values are already rates, so the axis is a percentage.
            axis=alt.Axis(format="+%", gridColor=PALETTE["line"], gridOpacity=0.6),
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
        tooltip=[
            alt.Tooltip("date:T", title="Date"),
            alt.Tooltip("series:N", title=None),
            alt.Tooltip("value:Q", title="Return", format="+.2%"),
        ],
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
# Centred via a wrapper div: an inline-block paragraph inside a text-align
# centre parent cannot be knocked out of alignment by Streamlit's own rules.
eyebrow("Read this before the numbers")
st.markdown(
    '<div style="text-align:center !important; width:100%;">'
    '<p style="display:inline-block; max-width:62ch; line-height:1.7;'
    'text-align:center !important; margin:0 auto !important;'
    'color:var(--hx-bone);">'
    "This record is short. The fund started in August 2026, and a few weeks of "
    "numbers tell you close to nothing — a good stretch this early is as "
    "likely to be luck as skill. The leveraged positions also mean the swings "
    "are wider than the returns suggest, so the drawdown is the number worth "
    "watching, not the total. We publish from the beginning rather than "
    "waiting for a flattering run to start from."
    "</p></div>",
    unsafe_allow_html=True,
)

footer()
