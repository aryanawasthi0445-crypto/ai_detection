import torch
import cv2
import numpy as np
from ultralytics import YOLO
from detector.violence_detector import ViolenceDetector
from detector.weapon_detector import WeaponDetector
from config.settings import PERSON_CLASS_ID, WEAPON_CLASSES, CONFIDENCE_THRESHOLD

class AIInferenceWrapper:
    """
    Unified wrapper for both Detection and Classification models.
    Integrates heuristic logic (Weapon/Proximity) with AI classification.
    """
    def __init__(self, det_model_path="yolov8n.pt", cls_model_path="yolov8n-cls.pt"):
        print(f"[INFO] Initializing Models...")
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        
        # Load Detection Model (for Bounding Boxes)
        self.det_model = YOLO(det_model_path)
        
        # Load Classification Model (for Violence/Non-Violence Label)
        self.cls_model = YOLO(cls_model_path)
        
        # Initialize Heuristic Detectors
        self.violence_heuristic = ViolenceDetector()
        self.weapon_heuristic = WeaponDetector()
        
        print(f"[INFO] Models loaded on {self.device}")

    def predict_frame(self, frame):
        """
        Processes a single frame:
        1. Runs Detection (Persons, Weapons)
        2. Runs Heuristic Logic (Proximity, Movement)
        3. Runs Classification (Violence/Non-Violence)
        """
        # OPTIMIZATION: Use imgsz=320 for significant CPU speedup
        inference_size = 320
        
        # 1. Detection Inference
        det_results = self.det_model(frame, device=self.device, verbose=False, imgsz=inference_size)[0]
        persons = []
        weapons = []
        
        if det_results.boxes:
            boxes = det_results.boxes.xyxy.cpu().numpy()
            confidences = det_results.boxes.conf.cpu().numpy()
            class_ids = det_results.boxes.cls.cpu().numpy().astype(int)

            for i, class_id in enumerate(class_ids):
                conf = float(confidences[i])
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
                    weapons.append(box)

        # 2. Heuristic Logic
        violence_alerts = self.violence_heuristic.analyze(persons)
        weapon_alerts = self.weapon_heuristic.analyze(persons, weapons)
        all_heuristic_alerts = list(set(violence_alerts + weapon_alerts))

        # 3. Classification Inference
        cls_results = self.cls_model(frame, device=self.device, verbose=False, imgsz=inference_size)[0]
        prediction = "non-violence"
        confidence = 0.0
        
        if cls_results.probs is not None:
            top1_idx = cls_results.probs.top1
            prediction = cls_results.names[top1_idx]
            confidence = float(cls_results.probs.top1conf)

        return {
            "prediction": prediction,
            "confidence": confidence,
            "detections": {
                "persons": persons,
                "weapons": weapons
            },
            "heuristic_alerts": all_heuristic_alerts
        }

    def warmup(self):
        """Pre-heats the models to avoid first-request lag."""
        dummy_frame = np.zeros((640, 640, 3), dtype=np.uint8)
        self.predict_frame(dummy_frame)
        print(f"[INFO] Models warmed up.")
