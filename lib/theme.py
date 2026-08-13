"""Design tokens and global styling for Haruspex Capital Partners.

Everything visual is defined here. Change a token in PALETTE or FONTS and it
propagates across every page — don't hardcode colors in the view files.
"""

import streamlit as st

# ---------------------------------------------------------------------------
# Tokens
# ---------------------------------------------------------------------------
# The palette is drawn from the Piacenza Liver: a bronze Etruscan artifact,
# oxidized to green, inscribed on bone-colored parchment maps.

PALETTE = {
    "ink": "#0E1216",        # page background — deep slate, not pure black
    "panel": "#161C22",      # raised surfaces
    "line": "#232B33",       # hairlines and dividers
    "bronze": "#B08A4F",     # primary accent — aged bronze
    "verdigris": "#4F8F7D",  # secondary accent — oxidized copper
    "bone": "#E6E1D5",       # primary text
    "ash": "#8A9299",        # secondary text
    "ember": "#B04A38",      # reserved for losses and warnings only
}

FONTS = {
    "display": "'Fraunces', Georgia, serif",
    "body": "'IBM Plex Sans', system-ui, sans-serif",
    "data": "'IBM Plex Mono', ui-monospace, monospace",
}

FONT_IMPORT = (
    "https://fonts.googleapis.com/css2"
    "?family=Fraunces:opsz,wght@9..144,400;9..144,600"
    "&family=IBM+Plex+Sans:wght@400;500;600"
    "&family=IBM+Plex+Mono:wght@400;500"
    "&display=swap"
)


def _css() -> str:
    p, f = PALETTE, FONTS
    return f"""
    :root {{
        --hx-ink: {p["ink"]};
        --hx-panel: {p["panel"]};
        --hx-line: {p["line"]};
        --hx-bronze: {p["bronze"]};
        --hx-verdigris: {p["verdigris"]};
        --hx-bone: {p["bone"]};
        --hx-ash: {p["ash"]};
        --hx-ember: {p["ember"]};
        --hx-display: {f["display"]};
        --hx-body: {f["body"]};
        --hx-data: {f["data"]};
    }}

    .stApp {{ background: var(--hx-ink); }}

    html, body, [class*="css"], .stMarkdown, p, li, span, div {{
        font-family: var(--hx-body);
        color: var(--hx-bone);
    }}

    h1, h2, h3 {{ font-family: var(--hx-display); font-weight: 600; }}

    /* Trim Streamlit's default chrome without hiding the menu entirely. */
    #MainMenu {{ visibility: hidden; }}
    footer {{ visibility: hidden; }}
    .block-container {{ padding-top: 3rem; max-width: 1080px; }}

    /* ---- Eyebrow: small caps section label -------------------------- */
    .hx-eyebrow {{
        font-family: var(--hx-data);
        font-size: 0.72rem;
        letter-spacing: 0.22em;
        text-transform: uppercase;
        color: var(--hx-bronze);
        margin-bottom: 0.75rem;
    }}

    /* ---- Type scale -------------------------------------------------- */
    .hx-display {{
        font-family: var(--hx-display);
        font-size: clamp(2.6rem, 7vw, 4.4rem);
        line-height: 1.02;
        letter-spacing: -0.02em;
        margin: 0 0 1rem 0;
    }}
    .hx-lede {{
        font-size: 1.15rem;
        line-height: 1.65;
        color: var(--hx-ash);
        max-width: 46ch;
    }}
    .hx-h2 {{
        font-family: var(--hx-display);
        font-size: 1.9rem;
        letter-spacing: -0.01em;
        margin: 0 0 0.9rem 0;
    }}
    .hx-body {{ line-height: 1.7; color: var(--hx-bone); max-width: 62ch; }}
    .hx-muted {{ color: var(--hx-ash); }}
    .hx-mono {{ font-family: var(--hx-data); }}

    /* ---- Hairline rule ---------------------------------------------- */
    .hx-rule {{
        border: 0;
        border-top: 1px solid var(--hx-line);
        margin: 3.5rem 0 2.25rem 0;
    }}

    /* ---- Panels ------------------------------------------------------ */
    .hx-panel {{
        background: var(--hx-panel);
        border: 1px solid var(--hx-line);
        padding: 1.5rem 1.6rem;
        height: 100%;
    }}
    .hx-panel h4 {{
        font-family: var(--hx-display);
        font-size: 1.1rem;
        margin: 0 0 0.5rem 0;
        color: var(--hx-bone);
    }}
    .hx-panel p {{ color: var(--hx-ash); font-size: 0.94rem; line-height: 1.6; margin: 0; }}

    /* ---- Stat block -------------------------------------------------- */
    .hx-stat-value {{
        font-family: var(--hx-data);
        font-size: 2rem;
        color: var(--hx-bronze);
        line-height: 1.1;
    }}
    .hx-stat-label {{
        font-family: var(--hx-data);
        font-size: 0.7rem;
        letter-spacing: 0.16em;
        text-transform: uppercase;
        color: var(--hx-ash);
        margin-top: 0.35rem;
    }}

    /* ---- Asset placeholder slot -------------------------------------- */
    .hx-slot {{
        border: 1px dashed var(--hx-line);
        background: repeating-linear-gradient(
            45deg, transparent, transparent 9px,
            rgba(176,138,79,0.035) 9px, rgba(176,138,79,0.035) 18px);
        display: flex;
        align-items: center;
        justify-content: center;
        font-family: var(--hx-data);
        font-size: 0.72rem;
        letter-spacing: 0.14em;
        text-transform: uppercase;
        color: var(--hx-ash);
        text-align: center;
        padding: 1rem;
    }}

    /* ---- Footer ------------------------------------------------------ */
    .hx-footer {{
        border-top: 1px solid var(--hx-line);
        margin-top: 4rem;
        padding-top: 1.5rem;
        font-size: 0.8rem;
        color: var(--hx-ash);
        line-height: 1.6;
    }}
    .hx-footer strong {{ color: var(--hx-bone); font-weight: 500; }}

    /* ---- Sidebar ----------------------------------------------------- */
    section[data-testid="stSidebar"] {{
        background: var(--hx-panel);
        border-right: 1px solid var(--hx-line);
    }}

    /* ---- Tables and inputs ------------------------------------------- */
    [data-testid="stDataFrame"] {{ font-family: var(--hx-data); }}
    .stTextInput input, .stTextArea textarea, .stSelectbox div[data-baseweb="select"] {{
        background: var(--hx-panel);
        border-color: var(--hx-line);
        color: var(--hx-bone);
        font-family: var(--hx-body);
    }}

    /* ---- Accessibility floor ----------------------------------------- */
    a {{ color: var(--hx-verdigris); }}
    a:focus-visible, button:focus-visible {{
        outline: 2px solid var(--hx-bronze);
        outline-offset: 2px;
    }}
    @media (prefers-reduced-motion: reduce) {{
        * {{ animation: none !important; transition: none !important; }}
    }}
    @media (max-width: 640px) {{
        .block-container {{ padding-top: 1.5rem; }}
    }}
    """


def apply_theme() -> None:
    """Inject the stylesheet. Call once at the top of every page.

    The font is loaded via a <link> tag rather than an @import inside the
    stylesheet: Streamlit Cloud strips @import from injected <style> blocks,
    which silently drops the display face back to a system sans.
    """
    st.markdown(
        '<link rel="preconnect" href="https://fonts.googleapis.com">'
        '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
        f'<link href="{FONT_IMPORT}" rel="stylesheet">',
        unsafe_allow_html=True,
    )
    st.markdown(f"<style>{_css()}</style>", unsafe_allow_html=True)
