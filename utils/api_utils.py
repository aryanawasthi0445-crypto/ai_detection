import cv2
import numpy as np
import base64
import logging
import sys

def setup_logging():
    """
    Configures standard logging for the application.
    """
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(message)s",
        handlers=[
            logging.StreamHandler(sys.stdout)
        ]
    )
    return logging.getLogger("ai_service")

def decode_image_base64(base64_str: str):
    """
    Decodes a base64 string into an OpenCV image (numpy array).
    """
    try:
        # Strip header if present
        if "," in base64_str:
            base64_str = base64_str.split(",")[1]
            
        img_data = base64.b64decode(base64_str)
        nparr = np.frombuffer(img_data, np.uint8)
        img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
        return img
    except Exception as e:
        raise ValueError(f"Failed to decode base64 image: {e}")

def decode_image_bytes(image_bytes: bytes):
    """
    Decodes raw image bytes into an OpenCV image (numpy array).
    """
    try:
        nparr = np.frombuffer(image_bytes, np.uint8)
        img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
        return img
    except Exception as e:
        raise ValueError(f"Failed to decode image bytes: {e}")
