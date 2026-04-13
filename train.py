import argparse
from ultralytics import YOLO
import os
import torch


def main():
    parser = argparse.ArgumentParser(description="Train YOLOv8 for Violence Detection")
    parser.add_argument("--task", type=str, choices=["detect", "classify"], default="classify",
                        help="Task type: 'detect' for bounding boxes, 'classify' for whole-image label")
    parser.add_argument("--epochs", type=int, default=50, help="Number of training epochs")
    parser.add_argument("--imgsz", type=int, default=640, help="Image size")
    parser.add_argument("--data", type=str, default="data", help="Path to data folder (for classify) or data.yaml (for detect)")
    parser.add_argument("--workers", type=int, default=0, help="Number of data loader workers (0 recommended for Windows)")
    
    args = parser.parse_args()

    # Load a model
    if args.task == "classify":
        model_name = "yolov8n-cls.pt"
    else:
        model_name = "yolov8n.pt"
    
    # Check data structure for classification
    if args.task == "classify":
        train_path = os.path.join(args.data, "train")
        val_path = os.path.join(args.data, "val")
        
        if not os.path.exists(train_path) or not os.path.exists(val_path):
            print(f"[WARNING] YOLOv8 classification requires 'train' and 'val' subfolders in {args.data}.")
            print(f"[INFO] Please organize your data as: {args.data}/train/violence, {args.data}/train/non-violence, etc.")
            # We could add an auto-split logic here if needed, but for now we'll just inform the user.
    
    print(f"[INFO] Initializing {args.task} training with {model_name}...")
    model = YOLO(model_name)

    # Detect device
    device = 0 if torch.cuda.is_available() else "cpu"
    if device == 0:
        print(f"[INFO] CUDA detected. Training on: {torch.cuda.get_device_name(0)}")
    else:
        print("[WARNING] CUDA not available. Training on CPU. This will be slow!")

    # Train the model
    results = model.train(
        data=args.data,
        epochs=args.epochs,
        imgsz=args.imgsz,
        device=device,
        name=f"violence_{args.task}_model"
    )

    print(f"[INFO] Training complete. Model saved in: {results.save_dir}")

    print("[INFO] Training complete. Results saved in 'runs/'.")

if __name__ == "__main__":
    main()
