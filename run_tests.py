"""Smoke test: execute every page and report any exception."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from streamlit.testing.v1 import AppTest

PAGES = ["views/home.py", "views/about.py", "views/holdings.py",
         "views/performance.py", "views/team.py", "views/contact.py"]

failed = False
for page in PAGES:
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)), page)
    try:
        at = AppTest.from_file(path, default_timeout=90).run()
        errs = [f"{type(e.value).__name__}: {e.value}" for e in at.exception]
        if errs:
            failed = True
        print(f"{page:26s} {'FAIL' if errs else 'ok'} {'; '.join(errs)}", flush=True)
    except Exception as e:
        failed = True
        print(f"{page:26s} CRASH {type(e).__name__}: {e}", flush=True)
sys.exit(1 if failed else 0)
