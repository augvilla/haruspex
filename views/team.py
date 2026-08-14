"""Team — the people, with room for headshots you haven't taken yet."""

import streamlit as st

from lib.components import (
    body, eyebrow, footer, heading, page_header, rule, section, slot,
)

# Edit this list and the page rebuilds itself. Order is the order shown.
MEMBERS = [
    {"name": "Augustine Villalobos", "role": "Founder & Managing Partner", "bio": "Northwestern University '28"},
    {"name": "First Last", "role": "Managing Partner", "bio": "Title"},
    {"name": "First Last", "role": "Managing Partner", "bio": "Title"},
    {"name": "First Last", "role": "Equity Analyst", "bio": "Title"},
    {"name": "First Last", "role": "Economic Analyst", "bio": "Title"},
    {"name": "First Last", "role": "Risk Manager", "bio": "Title"},
]

section()

eyebrow("Team")

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

footer()
