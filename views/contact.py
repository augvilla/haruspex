"""Contact — a form that currently goes nowhere, plus the direct channels."""

import streamlit as st

from lib.components import (
    body, eyebrow, footer, heading, page_header, panel, rule, section,
)

page_header(
    "Contact",
    "Get in touch",
    "REPLACE ME — who should write, and what to expect back. If you only "
    "respond during recruiting season, say so here.",
)

rule()

left, right = st.columns([1.2, 1], gap="large")

with left:
    eyebrow("Send a message")
    with st.form("contact", clear_on_submit=True):
        name = st.text_input("Name")
        email = st.text_input("Email")
        topic = st.selectbox(
            "Reason for writing",
            ["Joining the fund", "Research question", "Press", "Something else"],
        )
        message = st.text_area("Message", height=140)
        sent = st.form_submit_button("Send message")

    if sent:
        if not name or not email or not message:
            # Errors say what happened and how to fix it.
            st.error("Add your name, email, and a message before sending.")
        else:
            # TODO: wire this up. Two straightforward options:
            #   1. Streamlit secrets + smtplib to send yourself an email.
            #   2. Post to a Google Form or Formspree endpoint.
            # Until then this only confirms locally and stores nothing.
            st.success("Message received. Nothing is sent yet — see the TODO in views/contact.py.")

with right:
    eyebrow("Direct")
    panel("Email", "REPLACE ME — the address you actually check.")
    st.write("")
    panel("Meetings", "REPLACE ME — when and where the fund meets, if that's public.")
    st.write("")
    panel("Elsewhere", "REPLACE ME — LinkedIn, GitHub, or wherever the research lives.")

rule()

eyebrow("Note")
heading("Before you write about money")
body(
    "REPLACE ME — but keep a version of this. State plainly that the fund does "
    "not accept outside capital, or, if it does, that anyone interested should "
    "speak to the university and to a licensed professional first. This "
    "paragraph costs you nothing and prevents a conversation you do not want."
)

footer()
