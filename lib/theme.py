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
    # ital axis included: the hero epigraph uses real italics, not a
    # browser-synthesized oblique.
    "?family=Fraunces:ital,opsz,wght@0,9..144,400;0,9..144,600;1,9..144,400"
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

    /* Deliberately does NOT include span or div: Streamlit wraps heading
       text in an anchor <span>, and a bare span rule here would override the
       heading's display face from the inside. */
    html, body, .stMarkdown, p, li {{
        font-family: var(--hx-body);
        color: var(--hx-bone);
    }}
    .stApp {{ color: var(--hx-bone); }}

    /* Streamlit's own heading rules out-specify a bare class selector, so
       these need !important or the display face silently reverts to sans. */
    h1, h2, h3,
    [data-testid="stMarkdownContainer"] h1,
    [data-testid="stMarkdownContainer"] h2,
    [data-testid="stMarkdownContainer"] h3 {{
        font-family: var(--hx-display) !important;
        font-weight: 600;
    }}

    /* Trim Streamlit's default chrome without hiding the menu entirely. */
    #MainMenu {{ visibility: hidden; }}
    footer {{ visibility: hidden; }}
    .block-container {{ padding-top: 0; max-width: 1100px; }}

    /* ---- Eyebrow: small caps section label -------------------------- */
    .hx-eyebrow {{
        font-family: var(--hx-data) !important;
        font-size: 0.72rem;
        letter-spacing: 0.22em;
        text-transform: uppercase;
        color: var(--hx-bronze);
        margin-bottom: 0.75rem;
    }}

    /* ---- Type scale -------------------------------------------------- */
    .hx-display, h1.hx-display {{
        font-family: var(--hx-display) !important;
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
    .hx-h2, h2.hx-h2 {{
        font-family: var(--hx-display) !important;
        font-size: 1.9rem;
        letter-spacing: -0.01em;
        margin: 0 0 0.9rem 0;
    }}
    .hx-body {{ line-height: 1.7; color: var(--hx-bone); max-width: 62ch; }}
    /* Opt-in centring, used on About. Applied per call rather than globally so
       the Holdings and Performance intros stay left-aligned. */
    .hx-body-center {{
        line-height: 1.7;
        color: var(--hx-bone);
        max-width: 62ch;
        margin-left: auto;
        margin-right: auto;
        text-align: center;
    }}
    .hx-muted {{ color: var(--hx-ash); }}
    .hx-mono {{ font-family: var(--hx-data); }}

    /* ---- Hairline rule ---------------------------------------------- */
    .hx-rule {{
        border: 0;
        border-top: 1px solid var(--hx-line);
        margin: 3.5rem 0 2.25rem 0;
    }}

    /* ---- Panels ------------------------------------------------------
       :has() scopes this to rows that actually contain a panel, so the
       stretch never touches the stat row, the team grid, or the holdings
       layout. Without it, each card sizes to its own text and a long block
       leaves the others hanging. */
    [data-testid="stHorizontalBlock"]:has(.hx-panel) {{
        align-items: stretch;
    }}
    [data-testid="stColumn"]:has(.hx-panel) {{
        display: flex;
    }}
    [data-testid="stColumn"]:has(.hx-panel) > div {{
        width: 100%;
        display: flex;
        flex-direction: column;
    }}
    [data-testid="stColumn"]:has(.hx-panel) [data-testid="stVerticalBlock"],
    [data-testid="stColumn"]:has(.hx-panel) [data-testid="stMarkdown"],
    [data-testid="stColumn"]:has(.hx-panel) [data-testid="stMarkdownContainer"] {{
        height: 100%;
        display: flex;
        flex-direction: column;
        flex: 1 1 auto;
    }}
    [data-testid="stColumn"]:has(.hx-panel) .hx-panel {{
        flex: 1 1 auto;
    }}

    .hx-panel {{
        display: flex;
        flex-direction: column;
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

    /* ---- Ticker line inside a sleeve block --------------------------- */
    .hx-tickers {{
        font-family: var(--hx-data) !important;
        font-size: 0.78rem;
        letter-spacing: 0.1em;
        color: var(--hx-bronze);
        margin-top: 1rem;
        padding-top: 0.9rem;
        border-top: 1px solid var(--hx-line);
    }}

    /* ---- Stat block -------------------------------------------------- */
    .hx-stat-value {{
        font-family: var(--hx-data) !important;
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

    /* ---- Top navigation ---------------------------------------------
       Replaces the sidebar. A horizontal bar reads as a firm's website;
       a left rail reads as a dashboard. */
    header[data-testid="stHeader"] {{
        background: var(--hx-ink) !important;
        border-bottom: 1px solid var(--hx-line);
    }}
    [data-testid="stNavSectionHeader"], [data-testid="stTopNav"] {{
        background: transparent !important;
    }}
    [data-testid="stTopNav"] a, header[data-testid="stHeader"] a {{
        font-family: var(--hx-body) !important;
        font-size: 0.82rem !important;
        letter-spacing: 0.1em;
        text-transform: uppercase;
        color: var(--hx-ash) !important;
    }}
    [data-testid="stTopNav"] a:hover {{ color: var(--hx-bone) !important; }}

    /* ---- Full-bleed band ---------------------------------------------
       Breaks out of the centered content column to span the viewport. */
    .hx-bleed {{
        margin-left: calc(50% - 50vw);
        margin-right: calc(50% - 50vw);
        width: 100vw;
    }}

    /* ---- Hero ---------------------------------------------------------
       One idea, centered, with a great deal of air around it. The air is
       the point: it is what separates a firm's site from a dashboard. */
    .hx-hero {{
        padding: clamp(4.5rem, 15vh, 8.5rem) 1.5rem;
        text-align: center;
        border-top: 1px solid var(--hx-line);
        border-bottom: 1px solid var(--hx-line);
        background:
            radial-gradient(ellipse at 50% 0%,
                rgba(176,138,79,0.07), transparent 62%),
            var(--hx-panel);
    }}
    .hx-hero-name {{
        font-family: var(--hx-display) !important;
        font-size: clamp(3rem, 8.5vw, 6.5rem);
        line-height: 0.95;
        letter-spacing: -0.035em;
        margin: 0;
        color: var(--hx-bone);
    }}
    .hx-hero-quote {{
        font-family: var(--hx-display);
        font-style: italic;
        font-weight: 400;
        font-size: clamp(1.1rem, 1.85vw, 1.55rem);
        line-height: 1.5;
        color: var(--hx-bone);
        max-width: 46ch;
        margin: 2.25rem auto 0 auto;
    }}
    .hx-hero-attrib {{
        /* Matches the epigraph exactly — same face, size and colour. Only
           the slope differs. */
        font-family: inherit;
        font-size: inherit;
        color: inherit;
        font-style: normal;
        white-space: nowrap;
        margin-left: 0.4em;
    }}
    .hx-hero-cue {{
        font-family: var(--hx-data) !important;
        font-size: 0.75rem;
        letter-spacing: 0.28em;
        text-transform: uppercase;
        color: var(--hx-bronze);
        margin-top: 2.75rem;
    }}

    /* ---- Statement: the one large paragraph under the hero ----------- */
    .hx-statement {{
        font-size: clamp(1.15rem, 1.9vw, 1.45rem);
        line-height: 1.6;
        color: var(--hx-bone);
        max-width: 58ch;
        margin: 0;
    }}
    .hx-statement strong {{ font-weight: 600; color: var(--hx-bone); }}

    /* ---- Page header used by every interior page --------------------- */
    .hx-pagehead {{
        padding: clamp(2.5rem, 7vh, 4.5rem) 0 0 0;
    }}

    /* ---- Section spacing --------------------------------------------- */
    .hx-section {{ padding: clamp(3rem, 8vh, 5.5rem) 0 0 0; }}

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

    /* ---- Font override of last resort --------------------------------
       Streamlit ships its own heading styles that beat a plain class
       selector. These use a long selector chain, the literal font stack
       rather than a custom property, and sit last in the sheet so they win
       the cascade outright. If headings ever revert to sans, this is the
       block to check first. */
    .stApp h1, .stApp h2, .stApp h3,
    .stApp .hx-display, .stApp h1.hx-display,
    .stApp .hx-h2, .stApp h2.hx-h2,
    .stApp [data-testid="stMarkdownContainer"] h1,
    .stApp [data-testid="stMarkdownContainer"] h2,
    .stApp [data-testid="stMarkdownContainer"] h3,
    .stApp [data-testid="stMarkdownContainer"] h1.hx-display,
    .stApp [data-testid="stMarkdownContainer"] h2.hx-h2,
    .stApp [data-testid="stMarkdownContainer"] .hx-display,
    .stApp [data-testid="stMarkdownContainer"] .hx-h2 {{
        font-family: 'Fraunces', Georgia, 'Times New Roman', serif !important;
    }}

    /* Streamlit puts an anchor <span> inside every heading. Force it to
       inherit rather than pick up a font of its own. */
    .stApp h1 span, .stApp h2 span, .stApp h3 span,
    .stApp .hx-display span, .stApp .hx-h2 span,
    .stApp [data-testid="stMarkdownContainer"] h1 span,
    .stApp [data-testid="stMarkdownContainer"] h2 span {{
        font-family: inherit !important;
        font-weight: inherit !important;
        color: inherit !important;
    }}

    /* Streamlit's paragraph rule out-specifies a bare class, which kills the
       auto side-margins that centre the hero sentence. Force them back. */
    .stApp .hx-hero .hx-hero-quote,
    .stApp [data-testid="stMarkdownContainer"] .hx-hero-quote {{
        margin-left: auto !important;
        margin-right: auto !important;
        margin-top: 2.25rem !important;
        text-align: center !important;
        max-width: 46ch !important;
        font-style: italic !important;
    }}
    .stApp .hx-hero .hx-hero-attrib,
    .stApp [data-testid="stMarkdownContainer"] .hx-hero-attrib {{
        font-style: normal !important;
        font-family: inherit !important;
        font-size: inherit !important;
        color: inherit !important;
    }}

    .stApp .hx-hero .hx-hero-cue,
    .stApp [data-testid="stMarkdownContainer"] .hx-hero-cue {{
        text-align: center !important;
        margin-left: auto !important;
        margin-right: auto !important;
    }}

    .stApp .hx-body-center,
    .stApp [data-testid="stMarkdownContainer"] .hx-body-center,
    .stApp [data-testid="stMarkdownContainer"] p.hx-body-center {{
        margin-left: auto !important;
        margin-right: auto !important;
        text-align: center !important;
    }}

    .stApp .hx-eyebrow, .stApp .hx-mono, .stApp .hx-stat-value,
    .stApp .hx-stat-label, .stApp .hx-slot,
    .stApp [data-testid="stMarkdownContainer"] .hx-eyebrow,
    .stApp [data-testid="stMarkdownContainer"] .hx-stat-value {{
        font-family: 'IBM Plex Mono', ui-monospace, monospace !important;
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
