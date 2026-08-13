"""Haruspex Capital Partners — application entrypoint.

Run locally:      streamlit run streamlit_app.py
Deploy:           push to GitHub, then point Streamlit Community Cloud at this
                  file. No other configuration is required.

Navigation sits across the top rather than in a sidebar: a horizontal bar
reads as a firm's website, a left rail reads as an internal tool.

Pages live in views/. To add one, write the file and add a st.Page line below.
"""

import streamlit as st

from lib.theme import apply_theme

st.set_page_config(
    page_title="Haruspex Capital Partners",
    page_icon="assets/favicon.svg",
    layout="wide",
)

apply_theme()

PAGES = [
    st.Page("views/home.py", title="Home", default=True),
    st.Page("views/about.py", title="About"),
    st.Page("views/holdings.py", title="Holdings"),
    st.Page("views/performance.py", title="Performance"),
    st.Page("views/team.py", title="Team"),
    st.Page("views/contact.py", title="Contact"),
]

st.logo("assets/logo-placeholder.svg", size="large")

st.navigation(PAGES, position="top").run()
