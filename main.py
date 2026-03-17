import cv2
import time
import os

from utils.video_stream import VideoStream
from utils.visualization import Visualizer
from detector.yolo_detector import YOLODetector
from detector.violence_detector import ViolenceDetector
from detector.weapon_detector import WeaponDetector

from config.settings import SAVE_SCREENSHOTS, SCREENSHOT_DIR

import argparse

def main():
    parser = argparse.ArgumentParser(description="AI Detection System")
    parser.add_argument("--video", "-v", type=str, help="Path to video file for testing")
    parser.add_argument("--model", "-m", type=str, help="Path to custom model weights (.pt)")
    args = parser.parse_args()

    print("[INFO] Initializing AI Detection System...")

    # Initialize modules with optional overrides
    video_stream = VideoStream(source_override=args.video).start()
    yolo_detector = YOLODetector(model_path=args.model)
    violence_detector = ViolenceDetector()
    weapon_detector = WeaponDetector()
    
    # Check if stream opened successfully
    if video_stream.cap is None or not video_stream.cap.isOpened():
        print("[ERROR] Stream failed to initialize. Exiting.")
        return

    print("[INFO] System ready. Press 'q' to exit.")

    # FPS Calculation
    prev_time = 0

    try:
        while True:
            # 1. Read Frame
            ret, frame = video_stream.read()
            if not ret:
                break

            # 2. Process YOLO Inference
            persons, weapons = yolo_detector.process_frame(frame)

            # 3. Analyze Advanced Logic
            violence_alerts = violence_detector.analyze(persons)
            weapon_alerts = weapon_detector.analyze(persons, weapons)
            
            # Combine Alerts
            all_alerts = list(set(violence_alerts + weapon_alerts))

            # 4. Generate JSON Output String
            json_output = Visualizer.generate_json_output(persons, weapons, all_alerts)
            
            # Print JSON to terminal (as requested for backend processing)
            print(json_output)

            # 5. Visualizer Processing (Overlay UI)
            # People
            for p in persons:
                Visualizer.draw_bbox(frame, (p['x1'], p['y1'], p['x2'], p['y2']), "Person", Visualizer.COLOR_PERSON, p['conf'])
            
            # Weapons
            for w in weapons:
                Visualizer.draw_bbox(frame, (w['x1'], w['y1'], w['x2'], w['y2']), "Weapon", Visualizer.COLOR_WEAPON, w['conf'])
                
            # Global Alerts
            Visualizer.display_alerts(frame, all_alerts)

            # FPS
            current_time = time.time()
            fps = 1 / (current_time - prev_time) if prev_time > 0 else 0
            prev_time = current_time
            Visualizer.display_fps(frame, fps)

            # Bonus: Save screenshots on alert
            if SAVE_SCREENSHOTS and all_alerts:
                timestamp = int(time.time() * 1000)
                filename = os.path.join(SCREENSHOT_DIR, f"alert_{timestamp}.jpg")
                cv2.imwrite(filename, frame)

            # 6. Show OpenCV Window
            cv2.imshow("AI Real-Time Detection Feed", frame)

            # 7. Exit Handle (Wait for 'q')
            if cv2.waitKey(1) & 0xFF == ord('q'):
                print("[INFO] Termination requested by user.")
                break

    except Exception as e:
        print(f"[FATAL ERROR] An unexpected error occurred: {e}")
    finally:
        # Cleanup
        video_stream.release()
        cv2.destroyAllWindows()
        print("[INFO] Cleanup complete. Shutdown successful.")


if __name__ == "__main__":
    main()
