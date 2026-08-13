"""Home — the hero, the thesis, and three doors into the rest of the site."""

import streamlit as st

from lib.components import (
    body,
    eyebrow,
    footer,
    heading,
    panel,
    rule,
    slot,
    stat,
    templum,
)

# --- Hero -------------------------------------------------------------------
left, right = st.columns([1.25, 1], gap="large", vertical_alignment="center")

with left:
    eyebrow("Northwestern University · Est. 2026")
    st.markdown(
        '<h1 class="hx-display">Haruspex<br>Capital Partners</h1>',
        unsafe_allow_html=True,
    )
    st.markdown(
        '<p class="hx-lede">'
        "REPLACE ME — one or two sentences on what the fund does and why it "
        "exists. Say the strategy plainly. Resist the urge to write a mission "
        "statement."
        "</p>",
        unsafe_allow_html=True,
    )

with right:
    st.markdown(
        f'<div style="display:flex;justify-content:center">'
        f"{templum(size=300, filled=[1, 4, 6, 9, 11, 14])}</div>",
        unsafe_allow_html=True,
    )
    st.markdown(
        '<p class="hx-mono hx-muted" style="text-align:center;font-size:0.7rem;'
        'letter-spacing:0.14em;margin-top:0.75rem">THE TEMPLUM · XVI REGIONS</p>',
        unsafe_allow_html=True,
    )

rule()

# --- Numbers ----------------------------------------------------------------
eyebrow("At a glance")
c1, c2, c3, c4 = st.columns(4)
with c1:
    stat("—", "Capital under management")
with c2:
    stat("—", "Positions held")
with c3:
    stat("—", "Members")
with c4:
    stat("—", "Inception")

st.caption(
    "Replace each em-dash with a real figure, or delete the block until you "
    "have numbers worth showing."
)

rule()

# --- Three doors ------------------------------------------------------------
eyebrow("What we do")
heading("Read the structure, then take the position")

col1, col2, col3 = st.columns(3, gap="medium")
with col1:
    panel(
        "The screen",
        "REPLACE ME — how you find candidates. Name the actual filters you run.",
    )
with col2:
    panel(
        "The sizing",
        "REPLACE ME — how you decide position size, and what your maximum is.",
    )
with col3:
    panel(
        "The exit",
        "REPLACE ME — what makes you sell. This is the section people read most "
        "carefully, so make it specific.",
    )

rule()

# --- Banner slot ------------------------------------------------------------
eyebrow("Asset slot")
slot("BANNER IMAGE — 1600 × 500 — assets/banner.png", height=220)

footer()
