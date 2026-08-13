# Haruspex Capital Partners

Site for a student-run investment fund at Northwestern. Built with Streamlit so
it deploys from GitHub with no server, no build step, and no hosting bill.

## Run it locally

```bash
pip install -r requirements.txt
streamlit run streamlit_app.py
```

Opens on http://localhost:8501.

## Deploy it

1. Push this folder to a GitHub repo.
2. Go to share.streamlit.io, sign in with GitHub, click **New app**.
3. Point it at your repo and set the main file to `streamlit_app.py`.
4. Deploy. Pushes to `main` redeploy automatically.

## Where things live

```
streamlit_app.py     entrypoint — page registry and sidebar
lib/theme.py         every color, font, and CSS rule
lib/components.py    reusable pieces, including the templum graphic
views/               one file per page
data/                holdings.csv and performance.csv drive the pages
assets/              logos, banners, headshots (see assets/README.md)
run_tests.py         smoke test — runs every page, reports exceptions
```

## Filling it in

Search the project for `REPLACE ME`. Every one is a spot expecting real copy.

```bash
grep -rn "REPLACE ME" views/
```

The two data files drive the Holdings and Performance pages. Edit the CSVs
rather than the Python — the sixteen-region allocation map, the sleeve chart,
the position table, and every summary statistic all recompute from them.

Image placeholders render as dashed slots. Replace a `slot(...)` call with
`st.image("assets/your-file.png")` when the artwork exists.

## Design notes

The name refers to the Etruscan priest who forecast by reading internal
structure rather than surface. The field he read was divided into sixteen
regions mapped to divisions of the sky — that grid is the site's one signature
graphic, used on the home page as a mark and on the holdings page as a real
allocation map where each shaded region is roughly one-sixteenth of capital.

Palette is drawn from the Piacenza Liver, the bronze artifact the region system
comes from: aged bronze `#B08A4F` and oxidized verdigris `#4F8F7D` on slate
`#0E1216`, with bone `#E6E1D5` for text. Type is Fraunces for display, IBM Plex
Sans for body, IBM Plex Mono for anything numeric. Change these in
`lib/theme.py` and they propagate everywhere.

## Before this goes public

The footer disclaimer in `lib/components.py` and the note at the bottom of
`views/contact.py` are load-bearing, not decoration. A public page showing
holdings and performance reads differently from a private spreadsheet, so leave
both in and fill the contact-page note with something true about whether the
fund takes outside money.

## Test

```bash
python run_tests.py
```

Runs every page and exits non-zero if any raises.
