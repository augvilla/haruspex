"""Home — full-bleed hero, the numbers, then the supporting sections."""

import streamlit as st

from lib.components import (
    eyebrow,
    footer,
    hero,
    panel,
    rule,
    section,
    sleeve,
    stat,
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

# --- Strategy ---------------------------------------------------------------
eyebrow("Strategy")

col1, col2, col3 = st.columns(3, gap="medium")
with col1:
    panel(
        "Allocation",
        "We invest in the chokepoints of the AI build-out — compute, "
        "optics and power — and in the robotics and space infrastructure "
        "built upon them. We also hold crypto, which has topped out of a "
        "strong four-year cycle, plus pre-IPO Anthropic SPV exposure.",
    )
with col2:
    panel(
        "Management",
        "We are an actively managed fund. Capital is allocated principally "
        "to crypto assets, quantum computing, robotics and space technology, "
        "and AI infrastructure, with any remainder staked in altcoins. This "
        "portfolio is built deliberately on calculated risk.",
    )
with col3:
    panel(
        "Duration",
        "This is a high-risk portfolio. Rome grew by strategic planning and "
        "rapid execution, and so does this fund. We look constantly to the "
        "future, and we do not sell merely because a week went badly or "
        "because a position feels uncomfortable.",
    )

section()
rule()

# --- Sleeves ----------------------------------------------------------------
eyebrow("The book")
s1, s2 = st.columns(2, gap="medium")
with s1:
    sleeve(
        "Quantum Computing",
        "Pure-play exposure to quantum hardware, held through a leveraged fund that takes its position via swaps.",
        "IONQ · Rigetti · D-Wave · Quantum Computing",
    )
with s2:
    sleeve(
        "AI Infrastructure",
        "The compute, interconnect and optics the build-out runs on — the parts nothing else works without.",
        "NVIDIA · Astera Labs · Coherent · Lumentum",
    )

st.write("")

s3, s4 = st.columns(2, gap="medium")
with s3:
    sleeve(
        "Physical Infrastructure",
        "The hardware layer beneath it all: launch, vehicles, data centre power and the crews who build the grid.",
        "SpaceX · Tesla · Vertiv · Quanta Services",
    )
with s4:
    sleeve(
        "Digital assets",
        "A broad index of the major chains, held on a cycle view rather than as a trade, with eligible assets staked.",
        "Bitcoin · Etherium · XRP · Solana",
    )

section()

footer()
