"""Holdings — the sleeve chart and the position table, both driven by CSV."""

from pathlib import Path

import altair as alt
import pandas as pd
import streamlit as st

from lib.components import eyebrow, footer, rule, section
from lib.theme import FONTS, PALETTE

DATA = Path(__file__).resolve().parent.parent / "data" / "holdings.csv"

section()
eyebrow("Holdings")
st.markdown(
    '<p style="line-height:1.7; max-width:none !important; width:100% !important;'
    'margin:0 !important; text-align:left !important; color:var(--hx-bone);">'
    "Every position the fund holds, with the reason it was bought. Weights are "
    "stated as of the last rebalance and are refreshed on the thirteenth of "
    "each month; between those dates they drift with price. Cash is shown as a "
    "line of its own rather than netted out, so the figures below always sum to "
    "the whole book."
    "</p>",
    unsafe_allow_html=True,
)

rule()

# --- Load -------------------------------------------------------------------
try:
    holdings = pd.read_csv(DATA)
except FileNotFoundError:
    st.error(
        "No holdings file found. Add one at data/holdings.csv with columns: "
        "sleeve, ticker, name, weight, thesis."
    )
    st.stop()

# Coerce weight to a number first: a stray Unicode minus or stray character in
# the CSV would otherwise load the column as text and crash the chart later.
holdings["weight"] = pd.to_numeric(holdings["weight"], errors="coerce")
bad = holdings["weight"].isna().sum()
if bad:
    st.warning(
        f"{bad} row(s) in data/holdings.csv have a weight that is not a "
        "number and were dropped. Check for a Unicode minus (\u2212) instead "
        "of a hyphen."
    )
    holdings = holdings.dropna(subset=["weight"])

# Sort once, heaviest first — both the chart and the table inherit this.
holdings = holdings.sort_values("weight", ascending=False).reset_index(drop=True)

# --- Sleeves ----------------------------------------------------------------
eyebrow("By sleeve")

sleeves = (
    holdings.groupby("sleeve", as_index=False)["weight"]
    .sum()
    .sort_values("weight", ascending=False)
)

# Built with Altair rather than st.bar_chart: st.bar_chart ships with pan and
# zoom enabled, which lets the axis be dragged below zero. This chart has no
# selection or .interactive() call, so the scale is fixed to [0, max].
# The domain must reach below zero when a sleeve is negative — an
# unallocated-cash line goes negative whenever positions exceed the capital
# base. A domain pinned at zero would clamp that bar to nothing.
upper = float(sleeves["weight"].max()) * 1.15
lower = min(0.0, float(sleeves["weight"].min()) * 1.15)
chart = (
    alt.Chart(sleeves)
    .mark_bar(size=26, color=PALETTE["bronze"])
    .encode(
        y=alt.Y("sleeve:N", sort="-x", title=None,
                axis=alt.Axis(labelLimit=220)),
        x=alt.X(
            "weight:Q",
            title=None,
            scale=alt.Scale(domain=[lower, upper], nice=False, clamp=True),
            axis=alt.Axis(format="%", gridColor=PALETTE["line"], tickCount=6),
        ),
        tooltip=[
            alt.Tooltip("sleeve:N", title="Sleeve"),
            alt.Tooltip("weight:Q", title="Weight", format=".1%"),
        ],
    )
    .properties(height=max(140, 52 * len(sleeves)))
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

# --- Positions --------------------------------------------------------------
eyebrow("Positions")
display = holdings.assign(weight=holdings["weight"] * 100)
st.dataframe(
    display,
    hide_index=True,
    width="stretch",
    # No fixed widths: Streamlit sizes each column to its content, so a long
    # sleeve name like "Physical Infrastructure" is not clipped.
    column_config={
        "sleeve": st.column_config.TextColumn("Sleeve"),
        "ticker": st.column_config.TextColumn("Ticker"),
        "name": st.column_config.TextColumn("Name"),
        "weight": st.column_config.NumberColumn("Weight", format="%.1f%%"),
        "thesis": st.column_config.TextColumn("Why we own it"),
    },
)
st.caption("Holdings and allocations updated the 13th of every month.")

footer()
