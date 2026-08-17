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
section()

# --- Numbers ----------------------------------------------------------------
eyebrow("At a glance")
c1, c2, c3, c4 = st.columns(4)
with c1:
    stat("$1,000+", "Assets")
with c2:
    stat("4+", "Positions")
with c3:
    stat("Aug 2026", "Inception")
with c4:
    stat("1+", "Management")

rule()

# --- Strategy ---------------------------------------------------------------
eyebrow("Strategy")

col1, col2, col3 = st.columns(3, gap="medium")
with col1:
    panel(
        "Allocation",
        "We hold four positions. The largest is photonics: the optical parts "
        "that move data between chips and servers, now that copper is running "
        "into its physical limits. Alongside it sit quantum and machine-"
        "learning hardware, Tesla and SpaceX, and the largest crypto assets.",
    )
with col2:
    panel(
        "Management",
        "Four positions, managed actively, with no fixed weights. We would "
        "rather own a handful of things we can explain than a long list we "
        "cannot. One position carries leverage built into the fund itself; the "
        "rest do not, and the portfolio never borrows on margin.",
    )
with col3:
    panel(
        "Duration",
        "This is a high-risk portfolio. Rome grew by strategic planning and "
        "rapid execution, and so does this fund. We look constantly to the "
        "future, and we do not sell merely because a week went badly or "
        "because a position has become uncomfortable to hold.",
    )

rule()

# --- Sleeves ----------------------------------------------------------------
eyebrow("Target")
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
        "Bitcoin · Ethereum · XRP · Solana",
    )


footer()
