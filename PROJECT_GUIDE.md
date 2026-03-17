# AI Violence & Weapon Detection System - Project Guide

This guide provides a comprehensive overview of the AI Detection System, its features, testing strategies, and operational instructions.

## 1. Project Overview
The AI Violence & Weapon Detection System is designed to monitor video streams (webcam, files, or RTSP) in real-time. It uses YOLOv8 for object detection and custom heuristic/classification logic to identify potentially dangerous situations.

## 2. Key Features

### Real-Time Detection
- **Human Detection**: Identifies and tracks persons in the frame.
- **Weapon Detection**: Specifically looks for weapons (default: knives/COCO class 43).
- **Proximity Analysis**: Calculates distances between persons and weapons or between multiple persons to assess risk.

### Advanced Alerting Logic
- **Violence Heuristic**: Detects potential violence based on high-velocity movement and close proximity between individuals.
- **Weapon Proximity**: Triggers high-priority alerts when a weapon is detected near a person.
- **Visual Overlays**: Displays bounding boxes, class labels, confidence scores, and high-visibility alert banners on the video feed.

### Data & Training Pipeline
- **Automated Frame Extraction**: A utility to convert Kaggle/custom videos into image datasets.
- **Smart Data Mapping**: Automatically handles various folder naming conventions (e.g., `Violence`, `Normal`, `NonViolence`).
- **Auto-Split Logic**: Automatically separates videos into Training (80%) and Validation (20%) sets to ensure rigorous model evaluation.
- **Custom Training**: A dedicated script to train YOLOv8 classification or detection models.

### Developer & Support Tools
- **JSON Logging**: Outputs detection data in structured JSON format for backend integration.
- **Screenshot Logging**: Automatically saves frames when alerts are triggered (configurable).
- **Flexible CLI**: Test any video file or model weight via command-line arguments without editing code.

## 3. Testing Implementation

We have implemented a multi-layered testing strategy to ensure reliability:

### Unit Testing (`tests/test_detectors.py`)
- Tests the core logic of `ViolenceDetector` and `WeaponDetector` in isolation.
- Uses mock detection data to verify that alerts trigger correctly under specific mathematical conditions (proximity/velocity).

### Integration Testing (`tests/test_integration.py`)
- Verifies that the `Visualizer` correctly formats detection results into the expected JSON structure.
- Ensures data consistency between the AI modules and the reporting layer.

### CLI Video Testing (Functional)
- Allows manual verification of the entire pipeline using recorded `.mp4` files.
- **Main System**: `python main.py --video "test.mp4"`
- **Classification Model**: `python test_model.py --video "test.mp4" --model "best.pt"`

## 4. How to Run & Use the Project

### Initial Setup
1. **Environment**: Use Python 3.10 and activate the virtual environment (`.\venv\Scripts\activate`).
2. **Install**: `pip install -r requirements.txt`.

### Running the System
- **Webcam (Default)**: `python main.py`
- **Video File (CLI Override)**: `python main.py --video path/to/video.mp4`
- **Custom Model**: `python main.py --model path/to/custom_weights.pt`

### The Training Workflow (Kaggle Dataset)
1. **Collect Videos**: Place your videos in `videos/voilence/` and `videos/non voilence/`.
2. **Extract Frames**: Run `python extract_frames.py --interval 10`. This creates the `data/` folder with auto-split train/val sets.
3. **Train Model**: Run `python train.py --task classify`.
4. **Verify Model**: Run `python test_model.py --video "test.mp4" --model "runs/classify/train/weights/best.pt"`.

## 5. Directory Structure
- `detector/`: AI logic and YOLO wrappers.
- `utils/`: Video streaming and visualization helpers.
- `tests/`: Automated test suite.
- `docs/`: Detailed guides for testing and training.
- `videos/`: Input directory for training videos.
- `data/`: Extracted image datasets (auto-generated).
- `main.py`: Primary application entry point.
- `extract_frames.py`: Dataset preparation tool.
- `train.py`: Model training script.
- `test_model.py`: Specialized model verification script.
