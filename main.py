import logging
import os

import qrcode
from dotenv import load_dotenv

load_dotenv()
logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

logging.info("Starting QR code generation...")

data = os.getenv("QR_DATA_URL", "https://github.com/phase5lhcm")
qr_dir = os.getenv("QR_CODE_DIR", "qr_codes")
filename = os.getenv("QR_CODE_FILENAME", "qr.png")
fill_color = os.getenv("FILL_COLOR", "black")
back_color = os.getenv("BACK_COLOR", "white")

os.makedirs(qr_dir, exist_ok=True)

qr = qrcode.QRCode(version=1, box_size=10, border=5)
qr.add_data(data)
qr.make(fit=True)

img = qr.make_image(fill_color=fill_color, back_color=back_color)
img_path = os.path.join(qr_dir, filename)
img.save(img_path)

logging.info(f" QR code saved to: {img_path}")
