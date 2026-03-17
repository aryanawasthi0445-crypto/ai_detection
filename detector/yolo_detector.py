import torch
from ultralytics import YOLO
from config.settings import YOLO_MODEL, CONFIDENCE_THRESHOLD, PERSON_CLASS_ID, WEAPON_CLASSES

class YOLODetector:
    """
    Wrapper for Ultralytics YOLOv8. Handles model loading, device selection,
    and formats predictions cleanly for the application logic.
    """
    def __init__(self, model_path=None):
        actual_model = model_path if model_path else YOLO_MODEL
        print(f"[INFO] Loading YOLO model: {actual_model}")
        
        # Load the model -> it auto-downloads if not found
        self.model = YOLO(actual_model)
        
        # Attempt to use GPU if available, else fallback cleanly to CPU
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        print(f"[INFO] Using Device: {self.device}")
        
        if self.device == "cuda":
            print(f"[INFO] GPU Detected: {torch.cuda.get_device_name(0)}")
        else:
            print("[INFO] Running on CPU. Performance may be lower.")


    def process_frame(self, frame):
        """
        Runs inference on a single frame.
        Filters and groups detections into Persons and Weapons.
        """
        # Run YOLO inference
        results = self.model(frame, device=self.device, verbose=False)[0]
        
        persons = []
        weapons = []
        
        if not results.boxes:
            return persons, weapons
            
        # Parse detections
        boxes = results.boxes.xyxy.cpu().numpy()
        confidences = results.boxes.conf.cpu().numpy()
        class_ids = results.boxes.cls.cpu().numpy().astype(int)

        for i, class_id in enumerate(class_ids):
            conf = confidences[i]
            
            if conf < CONFIDENCE_THRESHOLD:
                continue
                
            box = {
                'x1': int(boxes[i][0]),
                'y1': int(boxes[i][1]),
                'x2': int(boxes[i][2]),
                'y2': int(boxes[i][3]),
                'conf': conf
            }
            
            if class_id == PERSON_CLASS_ID:
                persons.append(box)
            elif class_id in WEAPON_CLASSES:
                # We save all possible weapons to a common list
                # For standard yolov8 COCO, this is usually just the 'knife' class (43)
                weapons.append(box)
                
        return persons, weapons
