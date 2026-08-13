"""Haruspex Capital Partners — application entrypoint.

Run locally:      streamlit run streamlit_app.py
Deploy:           push to GitHub, then point Streamlit Community Cloud at this
                  file. No other configuration is required.

Pages live in views/. To add one, write the file and add a st.Page line below.
"""

import streamlit as st

from lib.theme import apply_theme

st.set_page_config(
    page_title="Haruspex Capital Partners",
    page_icon="assets/favicon.svg",
    layout="wide",
    initial_sidebar_state="expanded",
)

apply_theme()

PAGES = [
    st.Page("views/home.py", title="Home", icon=":material/home:", default=True),
    st.Page("views/about.py", title="About", icon=":material/menu_book:"),
    st.Page("views/holdings.py", title="Holdings", icon=":material/grid_view:"),
    st.Page("views/performance.py", title="Performance", icon=":material/show_chart:"),
    st.Page("views/team.py", title="Team", icon=":material/group:"),
    st.Page("views/contact.py", title="Contact", icon=":material/mail:"),
]

with st.sidebar:
    st.markdown(
        '<div style="font-family:var(--hx-display);font-size:1.25rem;'
        'line-height:1.2;padding:0.5rem 0 0.25rem 0">Haruspex</div>'
        '<div class="hx-eyebrow">Capital Partners</div>',
        unsafe_allow_html=True,
    )

st.navigation(PAGES).run()
