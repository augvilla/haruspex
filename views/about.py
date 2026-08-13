"""About — the name, the mandate, the constraints."""

import streamlit as st

from lib.components import body, eyebrow, footer, heading, panel, rule, slot

eyebrow("About")
st.markdown('<h1 class="hx-display">The name</h1>', unsafe_allow_html=True)

body(
    "A haruspex was the Etruscan and Roman priest who forecast by inspecting "
    "the internal structure of a thing rather than its surface. The field he "
    "read was divided into sixteen regions, each mapped to a division of the "
    "sky. REPLACE ME — say in one more sentence why that maps onto how you "
    "actually invest, and then stop. Naming stories are best kept short."
)

rule()

eyebrow("Mandate")
heading("What this fund is allowed to do")
body(
    "REPLACE ME — state the mandate as a set of rules rather than an "
    "aspiration. What can the fund hold? What is the maximum position size? "
    "What leverage is permitted? What is explicitly out of bounds? A written "
    "mandate is the single most useful document a student fund can produce, "
    "because it is what stops a good week from becoming a policy."
)

c1, c2, c3 = st.columns(3, gap="medium")
with c1:
    panel("Universe", "REPLACE ME — what instruments are eligible.")
with c2:
    panel("Limits", "REPLACE ME — position caps, leverage caps, sleeve caps.")
with c3:
    panel("Cadence", "REPLACE ME — how often you meet, vote, and rebalance.")

rule()

eyebrow("How decisions get made")
heading("Process")
body(
    "REPLACE ME — walk through what happens between someone having an idea and "
    "the fund owning it. Who writes the memo, who challenges it, who votes, "
    "and what threshold carries. Describe the process you actually run, not "
    "the one you wish you ran."
)

rule()

eyebrow("Asset slot")
slot("TEAM OR CAMPUS PHOTO — 1200 × 600 — assets/about.jpg", height=200)

footer()
