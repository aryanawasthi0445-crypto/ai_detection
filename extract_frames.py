import cv2
import os
import argparse
import random
from pathlib import Path

def extract_frames(video_path, output_dir, interval=10):
    """Extracts frames from a video file at a given interval."""
    if not os.path.exists(output_dir):
        os.makedirs(output_dir, exist_ok=True)

    cap = cv2.VideoCapture(str(video_path))
    if not cap.isOpened():
        print(f"[ERROR] Could not open video: {video_path}")
        return

    video_name = Path(video_path).stem
    count = 0
    saved_count = 0

    while True:
        ret, frame = cap.read()
        if not ret:
            break
        
        if count % interval == 0:
            frame_name = f"{video_name}_frame_{count}.jpg"
            save_path = os.path.join(output_dir, frame_name)
            cv2.imwrite(save_path, frame)
            saved_count += 1
        
        count += 1

    cap.release()
    return saved_count

def main():
    parser = argparse.ArgumentParser(description="Extract frames from videos with auto-split for YOLOv8 training.")
    parser.add_argument("--input", type=str, default="videos", help="Directory containing video subfolders")
    parser.add_argument("--output", type=str, default="data", help="Target directory for images")
    parser.add_argument("--interval", type=int, default=10, help="Extract every N-th frame")
    parser.add_argument("--split", type=float, default=0.8, help="Train/Val split ratio (default: 0.8)")
    
    args = parser.parse_args()

    # Flexible Mapping for Kaggle Datasets and User Preferences
    # Map common folder names to standard ones (using user's spelling if preferred)
    category_map = {
        "voilence": "voilence",
        "violence": "voilence",
        "non voilence": "non-voilence",
        "non-voilence": "non-voilence",
        "nonviolence": "non-voilence",
        "non-violence": "non-voilence",
        "normal": "non-voilence"
    }
    
    # Scan input directory for categories
    if not os.path.exists(args.input):
        print(f"[ERROR] Input directory '{args.input}' does not exist.")
        return

    found_dirs = [d for d in os.listdir(args.input) if os.path.isdir(os.path.join(args.input, d))]
    
    for d in found_dirs:
        # Determine standard category name
        std_name = category_map.get(d.lower(), d.lower())
        input_cat_dir = os.path.join(args.input, d)
        
        print(f"[INFO] Found category: {d} -> Mapping to: {std_name}")
        
        video_extensions = ['.mp4', '.avi', '.mov', '.mkv']
        all_videos = [f for f in Path(input_cat_dir).glob("**/*") if f.suffix.lower() in video_extensions]
        
        if not all_videos:
            print(f"[WARNING] No videos found in {input_cat_dir}")
            continue

        # Shuffle and Split
        random.shuffle(all_videos)
        split_idx = int(len(all_videos) * args.split)
        train_videos = all_videos[:split_idx]
        val_videos = all_videos[split_idx:]

        print(f"[INFO] Total: {len(all_videos)} | Train: {len(train_videos)} | Val: {len(val_videos)}")

        # Process Train
        for v in train_videos:
            out_dir = os.path.join(args.output, "train", std_name)
            extract_frames(v, out_dir, args.interval)
        
        # Process Val
        for v in val_videos:
            out_dir = os.path.join(args.output, "val", std_name)
            extract_frames(v, out_dir, args.interval)

    print("[INFO] Extraction and auto-splitting complete.")
    print(f"Dataset ready at: {args.output}")

if __name__ == "__main__":
    main()
