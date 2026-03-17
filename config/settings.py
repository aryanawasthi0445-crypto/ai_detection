# settings.py
import os

# Set execution mode. Options: 'webcam', 'video', 'rtsp'
MODE = "webcam"

# File & connection paths
VIDEO_FILE_PATH = "test.mp4"
RTSP_URL = "rtsp://username:password@ip:port/stream"

# Model selection. YOLOv8 nano is lightweight and best for real-time CPU operations
YOLO_MODEL = "yolov8n.pt"

# Object classes
# Note: standard YOLOv8 COCO models detect 'person'(0) and 'knife'(43). 
# 'gun' is not standard in 80 COCO classes, but we can simulate/placeholder logic for it if a fine-tuned model provides it.
PERSON_CLASS_ID = 0
WEAPON_CLASSES = [43]  # Knife class ID in standard COCO. You can add IDs if using a custom weapons model.

# Detection thresholds
CONFIDENCE_THRESHOLD = 0.4

# Logic constraints for alerting
VIOLENCE_PROXIMITY_THRESHOLD = 150  # Pixels: How close persons need to be to trigger proximity checks
VIOLENCE_RAPID_MOVEMENT_THRESHOLD = 50 # Pixels per frame
WEAPON_PROXIMITY_THRESHOLD = 100 # Pixels: How close a weapon is to a person to trigger alert

# Bonus: Detections logging
SAVE_SCREENSHOTS = False
SCREENSHOT_DIR = "alerts/"
if SAVE_SCREENSHOTS and not os.path.exists(SCREENSHOT_DIR):
    os.makedirs(SCREENSHOT_DIR)
