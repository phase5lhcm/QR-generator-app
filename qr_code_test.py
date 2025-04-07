import os

import pytest


def test_qr_code_file_creation():
    qr_dir = os.getenv("QR_CODE_DIR", "qr_codes")
    filename = os.getenv("QR_CODE_FILENAME", "qr.png")
    assert os.path.isfile(
        os.path.join(qr_dir, filename)
    ), "QR Code file was not created"
