import os

from dotenv import load_dotenv

load_dotenv()

data = os.getenv("QR_DATA_URL", "https://github.com/phase5lhcm")
qr_dir = os.getenv("QR_CODE_DIR", "qr_codes")
filename = os.getenv("QR_CODE_FILENAME", "qr.png")
fill_color = os.getenv("FILL_COLOR", "black")
back_color = os.getenv("BACK_COLOR", "white")
