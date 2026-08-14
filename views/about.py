"""About — the name, the mandate, the constraints.

Paragraphs are written inline rather than through a shared helper so this page
cannot break if lib/ is a different version. Inline !important beats
Streamlit's own paragraph rules, including its default max-width.
"""

import streamlit as st

from lib.components import eyebrow, footer, panel, rule, section

# No max-width: the paragraph runs the full width of the content column, so
# its edges line up with the section rules above and below it.
FULL = (
    "line-height:1.7; max-width:none !important; width:100% !important;"
    "margin:0 !important; text-align:left !important; color:var(--hx-bone);"
)


def para(text: str) -> None:
    """A body paragraph spanning the full content column."""
    st.markdown(f'<p style="{FULL}">{text}</p>', unsafe_allow_html=True)


section()
eyebrow("About")
para(
    "A haruspex was a Roman priest who read the future in the entrails of "
    "sacrificed animals — the liver above all, examined region by region for "
    "the will of the gods. We take the name for the method, not the "
    "superstition: the work is reading what a business is made of — where it "
    "sits in a supply chain, what stops functioning without it — rather than "
    "reading its price."
)

rule()

eyebrow("Mandate")
para(
    "The fund may hold listed equities, exchange-traded funds including "
    "leveraged and single-stock structures, and digital assets held directly "
    "or through an index vehicle. It may not use options, futures, or margin "
    "borrowed against the account: leverage enters the book only through the "
    "internal structure of a fund, never through the brokerage. Every position "
    "is entered with a written reason on file, and exits when that reason "
    "stops being true."
)

c1, c2, c3 = st.columns(3, gap="medium")
with c1:
    panel(
        "Universe",
        "Listed equities, ETFS including leveraged and "
        "single-stock structures, and digital assets. No options, futures, "
        "or margins.",
    )
with c2:
    panel(
        "Limits",
        "No position is entered at a size the fund could not afford to lose in "
        "full. Leveraged holdings are capped as a share of the book.",
    )
with c3:
    panel(
        "Cadence",
        "Positions are reviewed regularly and the book is rebalanced when a "
        "sleeve drifts materially from intent. Every transaction is logged.",
    )

rule()

eyebrow("The haruspex")
img_l, img_c, img_r = st.columns([1, 2, 1])
with img_c:
    st.image("assets/haruspex.png")

footer()
