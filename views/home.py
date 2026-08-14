"""Home — full-bleed hero, the numbers, then the supporting sections."""

import streamlit as st

from lib.components import (
    eyebrow,
    footer,
    heading,
    hero,
    panel,
    rule,
    section,
    slot,
    stat,
    templum,
)

# --- Hero: full bleed, centered, nothing but the name and the epigraph ------
hero(
    name="Haruspex Capital Partners",
    quote="Things do not signify because they have happened; "
          "they happen because they are going to signify.",
    attribution="— Seneca",
)

section()
rule()

# --- Numbers ----------------------------------------------------------------
eyebrow("At a glance")
c1, c2, c3, c4 = st.columns(4)
with c1:
    stat("$1,000", "Capital under management")
with c2:
    stat("1+", "Positions held")
with c3:
    stat("1+", "Members")
with c4:
    stat("Aug 2026", "Inception")

section()
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

section()
rule()

# --- The mark ---------------------------------------------------------------
eyebrow("The mark")
mark_l, mark_c, mark_r = st.columns([1, 1, 1])
with mark_c:
    st.markdown(
        f'<div style="display:flex;justify-content:center">'
        f"{templum(size=260, filled=[1, 4, 6, 9, 11, 14])}</div>",
        unsafe_allow_html=True,
    )
    st.markdown(
        '<p class="hx-mono hx-muted" style="text-align:center;font-size:0.7rem;'
        'letter-spacing:0.14em;margin-top:0.9rem">THE TEMPLUM · XVI REGIONS</p>',
        unsafe_allow_html=True,
    )

section()
rule()

eyebrow("Asset slot")
slot("BANNER IMAGE — 1600 × 500 — assets/banner.png", height=220)

footer()
