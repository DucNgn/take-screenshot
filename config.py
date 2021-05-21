import os
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()

SCREENSHOT_DIR = Path(os.getenv("SCREENSHOT_DIR", "./screenshots"))
