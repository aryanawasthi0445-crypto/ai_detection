import cv2
import argparse
from ultralytics import YOLO
import time

def main():
    parser = argparse.ArgumentParser(description="Test Classification Model on Video")
    parser.add_argument("--video", "-v", type=str, required=True, help="Path to video file")
    parser.add_argument("--model", "-m", type=str, required=True, help="Path to classification model (.pt)")
    parser.add_argument("--imgsz", type=int, default=640, help="Image size")
    args = parser.parse_args()

    print(f"[INFO] Loading model: {args.model}")
    model = YOLO(args.model)

    cap = cv2.VideoCapture(args.video)
    if not cap.isOpened():
        print(f"[ERROR] Could not open video: {args.video}")
        return

    print("[INFO] Starting test. Press 'q' to exit.")
    
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Inference
        results = model(frame, imgsz=args.imgsz, verbose=False)[0]
        
        # Parse Top-1 prediction
        probs = results.probs
        if probs is not None:
            top1_idx = probs.top1
            label = results.names[top1_idx]
            conf = float(probs.top1conf)
            
            # Draw overlay
            color = (0, 0, 255) if "violence" in label.lower() else (0, 255, 0)
            text = f"CLASS: {label.upper()} ({conf:.2%})"
            
            cv2.putText(frame, text, (20, 50), cv2.FONT_HERSHEY_SIMPLEX, 1.0, color, 3)

        cv2.imshow("Model Test - Classification", frame)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
    print("[INFO] Test complete.")

if __name__ == "__main__":
    main()
