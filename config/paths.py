import os
import pathlib

CELIAI_ROOT = pathlib.Path(os.environ["CELIAI"])
DATA = CELIAI_ROOT / "data"
MP3 = DATA / "mp3"
WAV = DATA / "wav"
SPECTROGRAMS = DATA / "spectrograms"
MODELS = CELIAI_ROOT / "models"
