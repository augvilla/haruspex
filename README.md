# Haruspex Capital Partners

A small, actively managed investment fund and the website that publishes its
book in the open.

The fund holds concentrated positions in the infrastructure behind the AI
build-out — compute, optics and power — alongside robotics and space
technology, quantum computing, and digital assets. It is deliberately
high-risk, and it says so on every page.

**Live at [haruspex.streamlit.app](https://haruspex.streamlit.app)**

## What the site does

Most funds publish a marketing page. This one publishes the book.

Every position is listed with the reason it was bought, weights and all, and
the record is shown from inception rather than from a flattering starting
point. Holdings and allocations are updated on the thirteenth of each month.
Where the numbers are too thin to mean anything — volatility on a two-week
track record, for instance — the site shows a dash instead of a figure.

The premise is that a fund willing to state its reasoning in public, before the
outcome is known, is easier to judge than one that explains itself afterward.

## The name

A haruspex was a Roman priest who read the future in the entrails of sacrificed
animals — the liver above all, examined region by region for the will of the
gods. The name is taken for the method rather than the superstition: reading
what a business is made of inside, where it sits in a supply chain and what
stops functioning without it, rather than reading its price.

## How it is built

A Streamlit application in Python, deployed from this repository with no
server, no build step and no hosting cost. Six pages, a shared component
library, and a single stylesheet that holds every colour and font.

The Holdings and Performance pages are entirely data-driven: the tables,
charts and summary statistics all compute from two CSV files, so updating the
fund means editing data rather than code. The contact form sends real mail
through credentials held in Streamlit secrets, which never touch this
repository.

Type is Fraunces for display and IBM Plex for body and figures. The palette —
aged bronze on slate — is drawn from the Piacenza Liver, the bronze Etruscan
artifact the sixteen-region reading system comes from.

```
streamlit_app.py     entrypoint and page registry
lib/theme.py         every colour, font and CSS rule
lib/components.py    shared page furniture
views/               one file per page
data/                holdings.csv and performance.csv drive the site
assets/              logo, favicon, illustration
run_tests.py         renders every page and reports any exception
```

## Disclaimer

Nothing in this repository or on the site it builds is an offer to sell or a
solicitation to buy any security, or investment advice of any kind. Figures
shown are for illustration and do not represent audited results. Past
performance does not predict future results.
