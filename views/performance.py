"""Performance — the NAV line, the summary statistics, the honest caveats."""

from pathlib import Path

import altair as alt
import pandas as pd
import streamlit as st

from lib.components import body, eyebrow, footer, heading, rule, stat
from lib.theme import FONTS, PALETTE

DATA = Path(__file__).resolve().parent.parent / "data" / "performance.csv"

eyebrow("Performance")
st.markdown('<h1 class="hx-display">The record</h1>', unsafe_allow_html=True)
body(
    "REPLACE ME — state the period covered, whether figures are net or gross "
    "of costs, and what the benchmark is and why you chose it. The numbers "
    "below are illustrative placeholder data until you swap in your own."
)

rule()

try:
    perf = pd.read_csv(DATA, parse_dates=["date"])
except FileNotFoundError:
    st.error(
        "No performance file found. Add one at data/performance.csv with "
        "columns: date, nav, benchmark."
    )
    st.stop()

# --- Summary statistics -----------------------------------------------------
returns = perf["nav"].pct_change().dropna()
total = perf["nav"].iloc[-1] / perf["nav"].iloc[0] - 1
bench_total = perf["benchmark"].iloc[-1] / perf["benchmark"].iloc[0] - 1
vol = returns.std() * (252 ** 0.5)
peak = perf["nav"].cummax()
max_dd = ((perf["nav"] - peak) / peak).min()

c1, c2, c3, c4 = st.columns(4)
with c1:
    stat(f"{total:+.1%}", "Total return")
with c2:
    stat(f"{total - bench_total:+.1%}", "vs benchmark")
with c3:
    stat(f"{vol:.0%}", "Annualized vol")
with c4:
    stat(f"{max_dd:.1%}", "Max drawdown")

rule()

# --- NAV chart --------------------------------------------------------------
eyebrow("Growth of 100")
heading("Fund against benchmark")

tidy = perf.melt("date", ["nav", "benchmark"], var_name="series", value_name="value")
tidy["series"] = tidy["series"].map({"nav": "Haruspex", "benchmark": "Benchmark"})

chart = (
    alt.Chart(tidy)
    .mark_line(strokeWidth=1.8)
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
                domain=["Haruspex", "Benchmark"],
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

# --- Caveats ----------------------------------------------------------------
eyebrow("Read this before the numbers")
body(
    "REPLACE ME — but keep something here. Note that the track record is "
    "short, that a leveraged book produces a return distribution with fat "
    "tails, and that drawdown matters more than total return over a period "
    "this brief. A performance page that volunteers its own weaknesses is "
    "read as more credible, not less."
)

footer()
