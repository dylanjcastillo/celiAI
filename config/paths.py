import os
import pathlib

CELIAI_ROOT = pathlib.Path(os.environ["CELIAI"])
DATA = CELIAI_ROOT / "data"
RAW = DATA / "raw"
INTERIM = DATA / "interim"
