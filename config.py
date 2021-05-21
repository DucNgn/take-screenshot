import os
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()

SCREENSHOT_DIR = Path(os.getenv("SCREENSHOT_DIR", "./screenshots"))
SCREENSHOT_DIR.mkdir(parents=True, exist_ok=True)

os.environ['WDM_LOG_LEVEL'] = '0' 
