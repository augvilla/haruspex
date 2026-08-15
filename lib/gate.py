"""A soft password gate, switched entirely from Streamlit secrets.

To take the site public, set enabled = false in the [auth] block of secrets —
or delete the block. No code change and no redeploy needed.

This deters casual visitors. It is not authentication: everyone shares one
password, there are no accounts, and the site's source is public. Do not put
anything behind it that would actually hurt you if it leaked.
"""

import hmac

import streamlit as st


def _config() -> dict | None:
    """Return the [auth] block, or None when the gate should be off."""
    try:
        cfg = st.secrets["auth"]
    except Exception:
        return None
    if not cfg.get("enabled", False):
        return None
    if not cfg.get("password"):
        return None
    return dict(cfg)


def require_password() -> None:
    """Block the app until the right password is entered. No-op when off."""
    cfg = _config()
    if cfg is None:
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
            # compare_digest rather than == : constant time, no length leak.
            if hmac.compare_digest(entered, str(cfg["password"])):
                st.session_state["_gate_open"] = True
                st.rerun()
            else:
                st.error("Not that one.")

    st.stop()
