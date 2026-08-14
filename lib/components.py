"""Reusable page pieces.

The signature element is the templum: the sixteen-region field an Etruscan
haruspex used to divide the sky before reading it. It appears once as the hero
mark and once more on the holdings page, where the sixteen regions carry real
allocation data. It is not used anywhere else — one motif, used twice, means
something; used everywhere it becomes wallpaper.
"""

import streamlit as st

from .theme import PALETTE


# ---------------------------------------------------------------------------
# Small primitives
# ---------------------------------------------------------------------------
def eyebrow(text: str) -> None:
    """Small-caps label that sits above a section heading."""
    st.markdown(f'<div class="hx-eyebrow">{text}</div>', unsafe_allow_html=True)


def rule() -> None:
    """Hairline divider between sections."""
    st.markdown('<hr class="hx-rule">', unsafe_allow_html=True)


def heading(text: str) -> None:
    st.markdown(f'<h2 class="hx-h2">{text}</h2>', unsafe_allow_html=True)


def body(text: str) -> None:
    st.markdown(f'<p class="hx-body">{text}</p>', unsafe_allow_html=True)


def panel(title: str, text: str) -> None:
    """Bordered card. Use inside a st.columns() row."""
    st.markdown(
        f'<div class="hx-panel"><h4>{title}</h4><p>{text}</p></div>',
        unsafe_allow_html=True,
    )


def sleeve(name: str, line: str, tickers: str) -> None:
    """One exposure sleeve: what it is, why, and the actual tickers.

    Tickers are set in the mono face and bronze so the eye can scan them
    without reading the prose — this block exists to answer "what specifically"
    at the moment the question forms.
    """
    st.markdown(
        f'<div class="hx-panel"><h4>{name}</h4><p>{line}</p>'
        f'<div class="hx-tickers">{tickers}</div></div>',
        unsafe_allow_html=True,
    )


def stat(value: str, label: str) -> None:
    """A single number with its label. Numbers are always monospace."""
    st.markdown(
        f'<div class="hx-stat-value">{value}</div>'
        f'<div class="hx-stat-label">{label}</div>',
        unsafe_allow_html=True,
    )


def slot(label: str, height: int = 180) -> None:
    """Placeholder for artwork you haven't made yet.

    Swap for st.image("assets/your-file.png") when the real asset exists.
    """
    st.markdown(
        f'<div class="hx-slot" style="height:{height}px">{label}</div>',
        unsafe_allow_html=True,
    )


def section() -> None:
    """Vertical breathing room between major blocks."""
    st.markdown('<div class="hx-section"></div>', unsafe_allow_html=True)


def hero(name: str, quote: str = "", attribution: str = "", cue: str = "") -> None:
    """Full-bleed opening band: the name, an epigraph, and the place.

    This is the single element that most distinguishes a firm's site from a
    dashboard, so it deliberately spans the full viewport and carries nothing
    else. The epigraph is set in true italic Fraunces, which is why the ital
    axis is requested in theme.FONT_IMPORT.
    """
    # Attribution rides inline at the end of the quote, in roman, so the
    # epigraph reads as one unit rather than two stacked lines.
    attrib_html = (
        f' <span class="hx-hero-attrib">{attribution}</span>' if attribution else ""
    )
    quote_html = (
        f'<p class="hx-hero-quote">{quote}{attrib_html}</p>' if quote else ""
    )
    cue_html = f'<div class="hx-hero-cue">{cue}</div>' if cue else ""
    st.markdown(
        f'<div class="hx-bleed"><div class="hx-hero">'
        f'<h1 class="hx-hero-name">{name}</h1>'
        f"{quote_html}{cue_html}"
        f"</div></div>",
        unsafe_allow_html=True,
    )


def page_header(label: str, title: str, lede: str = "") -> None:
    """Standard opening for every interior page: label, title, one paragraph."""
    lede_html = f'<p class="hx-lede">{lede}</p>' if lede else ""
    st.markdown(
        f'<div class="hx-pagehead">'
        f'<div class="hx-eyebrow">{label}</div>'
        f'<h1 class="hx-display">{title}</h1>'
        f"{lede_html}</div>",
        unsafe_allow_html=True,
    )


def statement(text: str) -> None:
    """The large paragraph that sits directly under the hero."""
    st.markdown(f'<p class="hx-statement">{text}</p>', unsafe_allow_html=True)


# ---------------------------------------------------------------------------
# Signature: the templum
# ---------------------------------------------------------------------------
def templum(size: int = 320, filled: list[int] | None = None) -> str:
    """Return the sixteen-region field as inline SVG.

    Args:
        size: rendered width and height in px.
        filled: region indices (0-15, reading left-to-right, top-to-bottom)
            to shade in bronze. On the home page this is decorative; on the
            holdings page each shaded region is a real position.
    """
    filled = filled or []
    bronze, verdigris, line = PALETTE["bronze"], PALETTE["verdigris"], PALETTE["line"]
    cell = 100 / 4
    parts: list[str] = []

    # Shaded regions sit underneath the grid lines.
    for idx in filled:
        row, col = divmod(idx, 4)
        parts.append(
            f'<rect x="{col * cell}" y="{row * cell}" width="{cell}" height="{cell}" '
            f'fill="{bronze}" opacity="0.14"/>'
        )

    # The four-by-four division.
    for i in range(1, 4):
        pos = i * cell
        parts.append(
            f'<line x1="{pos}" y1="0" x2="{pos}" y2="100" stroke="{line}" stroke-width="0.4"/>'
            f'<line x1="0" y1="{pos}" x2="100" y2="{pos}" stroke="{line}" stroke-width="0.4"/>'
        )

    # Double outer frame, the way boundary lines are drawn on the artifact.
    parts.append(
        f'<rect x="0" y="0" width="100" height="100" fill="none" '
        f'stroke="{bronze}" stroke-width="0.7"/>'
        f'<rect x="3" y="3" width="94" height="94" fill="none" '
        f'stroke="{bronze}" stroke-width="0.3" opacity="0.5"/>'
    )

    # The lituus — the augur's curved staff, used to mark out the field.
    parts.append(
        f'<path d="M 18 82 Q 50 78 62 46 Q 68 30 56 26 Q 46 23 44 34" '
        f'fill="none" stroke="{verdigris}" stroke-width="0.9" '
        f'stroke-linecap="round" opacity="0.9"/>'
        f'<circle cx="18" cy="82" r="1.6" fill="{verdigris}"/>'
    )

    return (
        f'<svg viewBox="0 0 100 100" width="{size}" height="{size}" '
        f'role="img" aria-label="The templum: a field divided into sixteen regions" '
        f'xmlns="http://www.w3.org/2000/svg">{"".join(parts)}</svg>'
    )


# ---------------------------------------------------------------------------
# Page furniture
# ---------------------------------------------------------------------------
def footer() -> None:
    """Site-wide footer. The disclaimer is not optional — leave it in."""
    st.markdown(
        """
        <div class="hx-footer">
          <strong>Haruspex Capital Partners</strong> &nbsp;·&nbsp;
          Chicago, Illinois, United States of America<br>
          Nothing on this site is an offer to sell or a solicitation to buy any
          security, or investment advice of any kind. Figures shown are for
          illustration and do not represent audited results. Past performance
          does not predict future results.
        </div>
        """,
        unsafe_allow_html=True,
    )


def page_setup(title: str) -> None:
    """Call at the top of every view: applies theme and sets the browser tab."""
    from .theme import apply_theme

    apply_theme()
    st.markdown(
        f'<span style="display:none">{title}</span>', unsafe_allow_html=True
    )
