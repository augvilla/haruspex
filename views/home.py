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
        "We look for chokepoints — companies whose product is hard to "
        "substitute anywhere in the AI compute stack, from interconnect and "
        "optics to the power feeding the racks. On the tactical side we screen "
        "large caps into earnings, checking whether a name has already run up "
        "into the print and whether the multiple is stretched enough that a "
        "beat still sells off. And we hold digital assets on conviction. "
        "Crypto peaked in October 2025 and has spent the time since "
        "consolidating against a fixed and shrinking issuance schedule. We "
        "think it re-rates from here, and we think this is what currency looks "
        "like next.",
    )
with col2:
    panel(
        "The sizing",
        "The book is actively managed rather than run to fixed weights. "
        "Exposure concentrates in quantum computing, AI infrastructure and the "
        "power that feeds it, digital assets, and a short list of single names "
        "tied to the compute supply chain. These sectors are correlated and we "
        "size them knowing it — a risk-off week moves all of them in the same "
        "direction at once. Leveraged instruments are sized as though the "
        "position could go to zero, because the daily-reset structure means it "
        "can.",
    )
with col3:
    panel(
        "The exit",
        "Let's be direct: this is a high-risk book. Leveraged instruments, "
        "frontier sectors, and assets that didn't exist twenty years ago. We "
        "are not trying to match an index and we are not interested in the "
        "kind of portfolio that never has a bad month. Rome wasn't built by "
        "people who wanted their money back. We sell when the reason we bought "
        "stops being true — not when a position gets uncomfortable, and not "
        "because one week went badly.",
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
