"""Holdings — the sixteen-region allocation map plus the position table."""

from pathlib import Path

import pandas as pd
import streamlit as st

from lib.components import (
    body, eyebrow, footer, heading, page_header, rule, section, templum,
)
from lib.theme import PALETTE

DATA = Path(__file__).resolve().parent.parent / "data" / "holdings.csv"

page_header(
    "Holdings",
    "The book",
    "REPLACE ME — one sentence on how to read this page, and how current the "
    "figures are. State the as-of date explicitly; a holdings page without one "
    "is worse than no holdings page.",
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

# --- Allocation map ---------------------------------------------------------
# Each of the sixteen regions is one percentage-point bucket of the book,
# rounded. Shaded regions are deployed capital; empty regions are not.
deployed = holdings.loc[holdings["ticker"] != "CASH", "weight"].sum()
lit = min(16, round(deployed * 16))

left, right = st.columns([1, 1.3], gap="large", vertical_alignment="center")
with left:
    st.markdown(
        f'<div style="display:flex;justify-content:center">'
        f"{templum(size=260, filled=list(range(lit)))}</div>",
        unsafe_allow_html=True,
    )
with right:
    eyebrow("Deployment")
    heading(f"{lit} of 16 regions")
    body(
        f"{deployed:.0%} of the book is deployed; the remainder is held in "
        "cash. Each shaded region is roughly one-sixteenth of capital. The "
        "map redraws itself from data/holdings.csv, so you never update it "
        "by hand."
    )

rule()

# --- Sleeves ----------------------------------------------------------------
eyebrow("By sleeve")
sleeves = (
    holdings.groupby("sleeve", as_index=False)["weight"]
    .sum()
    .sort_values("weight", ascending=False)
)
st.bar_chart(
    sleeves.set_index("sleeve"),
    horizontal=True,
    color=PALETTE["bronze"],
    height=260,
)

rule()

# --- Positions --------------------------------------------------------------
eyebrow("By position")
heading("Every line, with the reason it is there")
display = holdings.assign(weight=holdings["weight"] * 100)
st.dataframe(
    display,
    hide_index=True,
    width="stretch",
    column_config={
        "sleeve": st.column_config.TextColumn("Sleeve", width="small"),
        "ticker": st.column_config.TextColumn("Ticker", width="small"),
        "name": st.column_config.TextColumn("Name"),
        "weight": st.column_config.NumberColumn("Weight", format="%.1f%%"),
        "thesis": st.column_config.TextColumn("Why we own it", width="large"),
    },
)
st.caption(
    "Edit data/holdings.csv to change this table. Nothing here is hardcoded "
    "in the page."
)

footer()
