import os
import shutil
import random
from pathlib import Path

def split_data(source_dir, target_dir, split_ratio=0.8):
    source_dir = Path(source_dir)
    target_dir = Path(target_dir)
    
    # Define classes based on existing folders
    # User folders: 'voilence', 'non voilence'
    # We will map them to cleaner names: 'violence', 'non-violence'
    class_mapping = {
        "voilence": "violence",
        "non voilence": "non-violence"
    }

    for src_name, target_name in class_mapping.items():
        src_path = source_dir / src_name
        if not src_path.exists():
            print(f"[WARNING] Source directory {src_path} not found. Skipping.")
            continue
            
        # Get all image files
        files = [f for f in os.listdir(src_path) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.webp'))]
        random.shuffle(files)
        
        split_point = int(len(files) * split_ratio)
        train_files = files[:split_point]
        val_files = files[split_point:]
        
        # Create directories
        (target_dir / "train" / target_name).mkdir(parents=True, exist_ok=True)
        (target_dir / "val" / target_name).mkdir(parents=True, exist_ok=True)
        
        # Copy files
        print(f"[INFO] Splitting class '{src_name}' ({len(files)} files)...")
        for f in train_files:
            shutil.copy(src_path / f, target_dir / "train" / target_name / f)
        for f in val_files:
            shutil.copy(src_path / f, target_dir / "val" / target_name / f)
            
        print(f"  - Train: {len(train_files)} files")
        print(f"  - Val/Test: {len(val_files)} files")

if __name__ == "__main__":
    split_data("dataset", "data")
    print("\n[SUCCESS] Dataset successfully split into 'data/' directory.")
