# Assets

Drop real artwork here and swap the placeholder calls in the views.

| File | Used by | Suggested size |
|---|---|---|
| `favicon.svg` | `streamlit_app.py` (page icon) | square, any size |
| `logo-placeholder.svg` | sidebar / logo slot | ~520 × 140 |
| `banner.png` | `views/home.py` | 1600 × 500 |
| `about.jpg` | `views/about.py` | 1200 × 600 |
| `headshots/*.jpg` | `views/team.py` | 600 × 600, square crop |

To replace a placeholder, find the `slot(...)` call in the view and swap it:

```python
# before
slot("BANNER IMAGE — 1600 × 500 — assets/banner.png", height=220)

# after
st.image("assets/banner.png", use_container_width=True)
```

Keep the palette consistent with `lib/theme.py`: bronze `#B08A4F`,
verdigris `#4F8F7D`, bone `#E6E1D5` on slate `#0E1216`.
