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
eyebrow("Strategy")

col1, col2, col3 = st.columns(3, gap="medium")
with col1:
    panel(
        "Allocation",
        "We buy the chokepoints of the AI build-out: the chips, optics and "
        "power stations without which none of it runs. We also hold crypto, "
        "which topped out in October 2025 and has been grinding sideways "
        "against a supply that keeps shrinking.",
    )
with col2:
    panel(
        "Management",
        "No fixed weights — the book is managed actively. The weight sits in "
        "quantum computing, Musk's two companies and crypto, with the "
        "remainder in AI infrastructure and cash. These are one bet wearing "
        "four hats, and we size them accordingly.",
    )
with col3:
    panel(
        "Duration",
        "Let us be direct: this is a high-risk book and we are not trying to "
        "match an index. Rome was not built by people who wanted their money "
        "back. We sell when the reason we bought stops being true, not because "
        "a week went badly, and not because it feels uncomfortable.",
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
