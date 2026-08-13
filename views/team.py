"""Team — the people, with room for headshots you haven't taken yet."""

import streamlit as st

from lib.components import body, eyebrow, footer, heading, rule, slot

# Edit this list and the page rebuilds itself. Order is the order shown.
MEMBERS = [
    {"name": "REPLACE ME", "role": "Managing Partner", "bio": "One or two lines. Class year, concentration, what they cover."},
    {"name": "REPLACE ME", "role": "Chief Investment Officer", "bio": "One or two lines."},
    {"name": "REPLACE ME", "role": "Risk", "bio": "One or two lines."},
    {"name": "REPLACE ME", "role": "Research", "bio": "One or two lines."},
    {"name": "REPLACE ME", "role": "Research", "bio": "One or two lines."},
    {"name": "REPLACE ME", "role": "Operations", "bio": "One or two lines."},
]

eyebrow("Team")
st.markdown('<h1 class="hx-display">Who runs it</h1>', unsafe_allow_html=True)
body(
    "REPLACE ME — a line about how the team is structured and how someone "
    "joins it. If you recruit on a cycle, say when."
)

rule()

COLUMNS = 3
for start in range(0, len(MEMBERS), COLUMNS):
    row = MEMBERS[start : start + COLUMNS]
    cols = st.columns(COLUMNS, gap="medium")
    for col, member in zip(cols, row):
        with col:
            # Swap for st.image("assets/headshots/name.jpg") when you have one.
            slot("HEADSHOT · 600 × 600", height=200)
            st.markdown(
                f'<div style="margin-top:0.9rem">'
                f'<div class="hx-eyebrow" style="margin-bottom:0.3rem">{member["role"]}</div>'
                f'<div style="font-family:var(--hx-display);font-size:1.15rem">{member["name"]}</div>'
                f'<p style="color:var(--hx-ash);font-size:0.9rem;line-height:1.55;margin-top:0.4rem">'
                f'{member["bio"]}</p></div>',
                unsafe_allow_html=True,
            )
    st.write("")

rule()

eyebrow("Joining")
heading("How to get involved")
body(
    "REPLACE ME — the application process, the time commitment, and what you "
    "expect from a new member in their first quarter. Be concrete about the "
    "workload; it filters better than any application question."
)

footer()
