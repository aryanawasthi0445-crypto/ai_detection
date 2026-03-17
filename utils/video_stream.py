import cv2
import sys
import os

from config.settings import MODE, VIDEO_FILE_PATH, RTSP_URL


class VideoStream:
    """
    Robust video capture handler to stream frames from Webcam, Video File, or RTSP.
    Includes fallbacks and error handling for bad hardware connections.
    """
    def __init__(self, source_override=None):
        self.cap = None
        self.mode = MODE
        self.source_override = source_override
        self.source = self._determine_source()

    def _determine_source(self):
        """Returns the appropriate OpenCV source string/int based on mode."""
        if self.source_override:
            # If override is a digit, treat as camera index
            if str(self.source_override).isdigit():
                return int(self.source_override)
            return self.source_override

        if self.mode == "webcam":
            return 0
        elif self.mode == "video":
            if not os.path.exists(VIDEO_FILE_PATH):
                print(f"[ERROR] Video file '{VIDEO_FILE_PATH}' not found.")
                print("[INFO] Falling back to webcam...")
                self.mode = "webcam"
                return 0
            return VIDEO_FILE_PATH
        elif self.mode == "rtsp":
            return RTSP_URL
        else:
            print(f"[ERROR] Unknown mode '{self.mode}'. Defaulting to webcam.")
            self.mode = "webcam"
            return 0

    def start(self):
        """Initializes the OpenCV VideoCapture object."""
        print(f"[INFO] Starting video stream for mode: {self.mode}")
        self.cap = cv2.VideoCapture(self.source)

        if not self.cap.isOpened():
            print(f"[ERROR] Failed to open '{self.mode}' at source: {self.source}")
            
            # If default webcam fails, try an alternative index as a safety net
            if self.mode == "webcam" and self.source == 0:
                print("[INFO] Attempting to find secondary camera at index 1...")
                self.cap = cv2.VideoCapture(1)
                if not self.cap.isOpened():
                    print("[ERROR] No working cameras found. Terminating.")
                    sys.exit(1)
            else:
                print("[ERROR] Ensure file exists or camera permissions are granted.")
                sys.exit(1)
                
        # Optional: Set camera resolution to 720p for a balance of speed/quality
        if self.mode == "webcam":
            self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
            self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
            
        return self

    def read(self):
        """Reads a frame from the capture source. Handles stream closure."""
        if self.cap is None:
            return False, None

        ret, frame = self.cap.read()
        if not ret:
            if self.mode == "video":
                print("[INFO] Video file ended.")
            else:
                print("[ERROR] Frame read failed (Connection lost).")
            return False, None
            
        return True, frame

    def release(self):
        """Releases the camera and destroys windows cleanly."""
        if self.cap is not None:
            self.cap.release()
            print("[INFO] Video stream stopped.")
