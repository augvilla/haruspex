"""Contact — a form that sends real mail via SMTP credentials in st.secrets.

The address never appears in the rendered page, so scrapers cannot harvest it.
If the secrets are missing the form degrades to a clear error rather than
pretending to have sent something.
"""

import re
import smtplib
from email.message import EmailMessage

import streamlit as st

from lib.components import eyebrow, footer, heading, rule, section

PARA = (
    "line-height:1.7; max-width:none !important; width:100% !important;"
    "margin:0 !important; text-align:left !important; color:var(--hx-bone);"
)


def para(text: str) -> None:
    st.markdown(f'<p style="{PARA}">{text}</p>', unsafe_allow_html=True)


def mail_config() -> dict | None:
    """Return the email block from secrets, or None if it isn't configured."""
    try:
        cfg = st.secrets["email"]
        required = ("address", "smtp_server", "smtp_port", "username", "password")
        if all(k in cfg for k in required):
            return dict(cfg)
    except Exception:
        pass
    return None


def send(cfg: dict, name: str, sender: str, reason: str, message: str) -> None:
    """Send the enquiry. Raises on failure so the caller can report it."""
    msg = EmailMessage()
    msg["Subject"] = f"Haruspex — {reason} — {name}"
    msg["From"] = cfg["username"]
    msg["To"] = cfg["address"]
    msg["Reply-To"] = sender
    msg.set_content(
        f"From: {name} <{sender}>\nReason: {reason}\n\n{message}"
    )
    with smtplib.SMTP_SSL(cfg["smtp_server"], int(cfg["smtp_port"])) as server:
        server.login(cfg["username"], cfg["password"])
        server.send_message(msg)


section()
eyebrow("Contact")
heading("Get in touch")
para(
    "Write if you want to join the fund, ask about a position, or challenge "
    "something on this site. One person reads this inbox, so replies are not "
    "instant, but they are real."
)

st.write("")

cfg = mail_config()

with st.form("contact", clear_on_submit=True):
    name = st.text_input("Name")
    sender = st.text_input("Your email")
    reason = st.selectbox(
        "Reason for writing",
        ["Joining the fund", "A position", "Something on this site", "Other"],
    )
    message = st.text_area("Message", height=150)
    submitted = st.form_submit_button("Send")

if submitted:
    if not name.strip() or not message.strip():
        st.error("Add your name and a message before sending.")
    elif not re.match(r"^[^@\s]+@[^@\s]+\.[^@\s]+$", sender.strip()):
        st.error("That email address does not look right — check it and resend.")
    elif cfg is None:
        st.error(
            "Mail is not configured on this deployment, so nothing was sent. "
            "Add an [email] block to Streamlit secrets."
        )
    else:
        try:
            send(cfg, name.strip(), sender.strip(), reason, message.strip())
            st.success("Sent. You'll get a reply at the address you gave.")
        except Exception:
            # Never surface the exception text: it can leak the host or user.
            st.error("That didn't send. Try again shortly.")

rule()

eyebrow("Note")
heading("Before you write about money")
para(
    "The fund pools contributions from its own members and does not take "
    "capital from anyone outside that group. If that ever changes, it will "
    "change here first, and anyone considering it should speak to a licensed "
    "professional rather than to us. Nothing on this site is an offer, a "
    "solicitation, or advice of any kind."
)

footer()
