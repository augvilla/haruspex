"""About — the name, the mandate, the constraints."""

import streamlit as st

from lib.components import (
    body, eyebrow, footer, heading, page_header, panel, rule, section,
)

section()

eyebrow("About")
body(
    "A haruspex was a Roman priest who read the future in the entrails of "
    "sacrificed animals — the liver above all, examined region by region for "
    "the will of the gods. We take the name for the method, not the superstition: "
    "the work is reading what a business is made of — where it sits in a supply chain, "
    "what stops functioning without it — rather than reading its price.",
)

rule()

eyebrow("Mandate")
body(
    "The fund may hold listed equities, exchange-traded funds including "
    "leveraged and single-stock structures, and digital assets held directly "
    "or through an index vehicle. It may not use options, futures, or margin "
    "borrowed against the account: leverage enters the book only through the "
    "internal structure of a fund, never through the brokerage. Every position "
    "is entered with a written reason on file, and exits when that reason stops "
    "being true."
)

c1, c2, c3 = st.columns(3, gap="medium")
with c1:
    panel("Universe", "Listed equities, exchange-traded funds including leveraged and single-stock structures, and digital assets. No options, no futures, no margin.")
with c2:
    panel("Limits", "No position is entered at a size the fund could not afford to lose in full. Leveraged holdings are capped as a share of the book.")
with c3:
    panel("Cadence", "Positions are reviewed regularly and the book is rebalanced when a sleeve drifts materially from intent. Every transaction is logged.")

rule()

eyebrow("Process")
body(
    "Every position begins as a written note: what the business does, why it is hard "
    "to replace, what would have to be true for the thesis to fail, and what the fund "
    "is prepared to lose. The note is written before the trade rather than after it, so "
    "the reason on file is the reason at entry and not one reconstructed later. Trades "
    "are logged one row per round trip and reviewed against the original note when they "
    "close. The fund is small enough that one person makes the call, which makes the written "
    "record the only real check on it."
)

rule()

eyebrow("The haruspex")
img_l, img_c, img_r = st.columns([1, 2, 1])
with img_c:
    st.image("assets/haruspex.png")

footer()
