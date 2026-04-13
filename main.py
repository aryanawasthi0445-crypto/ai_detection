import argparse
import uvicorn
import cv2
import time
import os

from utils.video_stream import VideoStream
from utils.visualization import Visualizer
from detector.yolo_detector import YOLODetector
from detector.violence_detector import ViolenceDetector
from detector.weapon_detector import WeaponDetector
from config.settings import SAVE_SCREENSHOTS, SCREENSHOT_DIR

def run_webcam_mode(video_path=None, model_path=None):
    print("[INFO] Starting Webcam Mode...")
    
    # Initialize modules
    video_stream = VideoStream(source_override=video_path).start()
    yolo_detector = YOLODetector(model_path=model_path)
    violence_detector = ViolenceDetector()
    weapon_detector = WeaponDetector()
    
    if video_stream.cap is None or not video_stream.cap.isOpened():
        print("[ERROR] Stream failed to initialize.")
        return

    print("[INFO] System ready. Press 'q' to exit.")
    prev_time = 0

    try:
        while True:
            ret, frame = video_stream.read()
            if not ret:
                break

            # 1. Detection
            persons, weapons = yolo_detector.process_frame(frame)

            # 2. Heuristic Analysis
            violence_alerts = violence_detector.analyze(persons)
            weapon_alerts = weapon_detector.analyze(persons, weapons)
            all_alerts = list(set(violence_alerts + weapon_alerts))

            # 3. JSON Output
            json_output = Visualizer.generate_json_output(persons, weapons, all_alerts)
            print(json_output)

            # 4. Rendering
            for p in persons:
                Visualizer.draw_bbox(frame, (p['x1'], p['y1'], p['x2'], p['y2']), "Person", Visualizer.COLOR_PERSON, p['conf'])
            for w in weapons:
                Visualizer.draw_bbox(frame, (w['x1'], w['y1'], w['x2'], w['y2']), "Weapon", Visualizer.COLOR_WEAPON, w['conf'])
            
            Visualizer.display_alerts(frame, all_alerts)
            
            current_time = time.time()
            fps = 1 / (current_time - prev_time) if prev_time > 0 else 0
            prev_time = current_time
            Visualizer.display_fps(frame, fps)

            if SAVE_SCREENSHOTS and all_alerts:
                timestamp = int(time.time() * 1000)
                filename = os.path.join(SCREENSHOT_DIR, f"alert_{timestamp}.jpg")
                cv2.imwrite(filename, frame)

            cv2.imshow("AI Real-Time Detection Feed", frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
    finally:
        video_stream.release()
        cv2.destroyAllWindows()
        print("[INFO] Webcam mode shutdown.")

def main():
    parser = argparse.ArgumentParser(description="AI Detection System Entry Point")
    parser.add_argument("--mode", type=str, choices=["api", "webcam"], default="api", 
                        help="Execution mode: 'api' for FastAPI server, 'webcam' for local GUI")
    parser.add_argument("--video", "-v", type=str, help="Path to video file (webcam mode only)")
    parser.add_argument("--model", "-m", type=str, help="Path to custom weights (webcam mode only)")
    parser.add_argument("--port", type=int, default=8000, help="Port for API mode")
    parser.add_argument("--host", type=str, default="0.0.0.0", help="Host for API mode")
    
    args = parser.parse_args()

    if args.mode == "api":
        print(f"[INFO] Starting API server on {args.host}:{args.port}")
        uvicorn.run("api:app", host=args.host, port=args.port, reload=False)
    else:
        run_webcam_mode(video_path=args.video, model_path=args.model)

if __name__ == "__main__":
    main()
