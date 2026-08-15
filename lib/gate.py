"""A soft password gate, switched entirely from Streamlit secrets.

To take the site public, set enabled = false in the [auth] block of secrets —
or delete the block. No code change and no redeploy needed.

Accepts either one shared password or a named table of them:

    [auth]
    enabled = true
    password = "one-shared-password"

or

    [auth]
    enabled = true

    [auth.passwords]
    augustine = "..."
    sam       = "..."

With a named table, whoever matched is kept in session state, so a password can
be revoked for one person without disturbing anyone else.

This deters casual visitors. It is not authentication: there are no accounts,
and the site's source is public. Do not put anything behind it that would
actually hurt you if it leaked.
"""

import hmac

import streamlit as st


def _entries() -> dict[str, str] | None:
    """Return {label: password}, or None when the gate should be off."""
    try:
        cfg = st.secrets["auth"]
    except Exception:
        return None
    if not cfg.get("enabled", False):
        return None

    named = cfg.get("passwords")
    if named:
        entries = {str(k): str(v) for k, v in dict(named).items() if v}
        return entries or None

    single = cfg.get("password")
    return {"guest": str(single)} if single else None


def _match(entered: str, entries: dict[str, str]) -> str | None:
    """Return the label whose password matches, checking all of them."""
    found = None
    for label, secret in entries.items():
        # compare_digest for each: constant time, and no early exit that
        # would let response timing reveal which label matched.
        if hmac.compare_digest(entered, secret):
            found = label
    return found


def require_password() -> None:
    """Block the app until a valid password is entered. No-op when off."""
    entries = _entries()
    if entries is None:
        return

    if st.session_state.get("_gate_open"):
        return

    st.markdown(
        '<div style="text-align:center; padding:4rem 1rem 2rem 1rem;">'
        '<div style="font-family:var(--hx-display); font-size:2.5rem;'
        ' color:var(--hx-bone);">Haruspex Capital Partners</div>'
        '<div style="font-family:var(--hx-data); font-size:0.75rem;'
        ' letter-spacing:0.22em; text-transform:uppercase;'
        ' color:var(--hx-bronze); margin-top:1rem;">Private preview</div>'
        "</div>",
        unsafe_allow_html=True,
    )

    left, middle, right = st.columns([1, 1.2, 1])
    with middle:
        with st.form("gate"):
            entered = st.text_input("Password", type="password")
            ok = st.form_submit_button("Enter")
        if ok:
            label = _match(entered, entries)
            if label:
                st.session_state["_gate_open"] = True
                st.session_state["_gate_label"] = label
                st.rerun()
            else:
                st.error("Not that one.")

    st.stop()
