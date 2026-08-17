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
        "into its physical limits. Alongside it sit quantum computing hardware "
        "and software, Tesla and SpaceX, and the largest crypto assets.",
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
        "Photonics & Optics",
        "The optical parts that carry data between chips and servers, now "
        "that copper is running into its physical limits.",
        "Lumentum · AXT Inc · Coherent · Anthropic",
    )
with s2:
    sleeve(
        "Quantum Computing",
        "Thirteen companies whose business is quantum itself, actively "
        "managed and concentrated rather than indexed.",
        "IonQ · Quantinuum · D-Wave · Infleqtion",
    )

st.write("")

s3, s4 = st.columns(2, gap="medium")
with s3:
    sleeve(
        "Aerospace and Robotics",
        "Tesla and SpaceX in a single position: automation on the ground "
        "and launch capacity above it.",
        "SpaceX · Tesla · Starlink · Optimus",
    )
with s4:
    sleeve(
        "Digital Assets",
        "The ten largest crypto assets by market value, rebalanced monthly "
        "and held on a cycle view.",
        "Bitcoin · Ethereum · XRP · Solana",
    )

footer()
