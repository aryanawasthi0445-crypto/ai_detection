# AI Detection Project - Testing Guide

There are several ways to test your project, ranging from individual component validation to full system integration.

## 1. Unit Testing
Test individual functions and classes in isolation. This is the fastest and most reliable way to catch logic errors.
- **Tools**: `pytest`, `unittest`.
- **Targets**: `ViolenceDetector`, `WeaponDetector`, `VideoStream` logic.
- **Example**: Feed `ViolenceDetector` a list of persons that are close together and moving fast, then verify it returns "Violence Detected".

## 2. Integration Testing
Test how multiple components work together.
- **Tools**: `pytest`.
- **Targets**: The pipeline of `YOLODetector` -> `ViolenceDetector` -> `Visualizer`.
- **Example**: Mock a video frame, pass it through the detector, and verify the resulting JSON output contains the expected fields.

## 3. Functional / End-to-End (E2E) Testing
Test the entire application as a user would.
- **Method**: Run `main.py` using a known video file instead of a live webcam.
- **Verification**: Check if screenshots are saved in `SCREENSHOT_DIR` when an event is triggered.

## 4. Static Analysis
Check code quality and type safety without running the code.
- **Tools**: `pyright`, `pylint`, `flake8`.
- **Benefit**: Catches `ImportError`, undefined variables, and type mismatches early.

## 5. Performance Benchmarking
Measure the efficiency of your AI models and processing loop.
- **Metric**: Frames Per Second (FPS), Inference latency (ms).
- **Target**: Ensure the system runs in real-time on your hardware.

## 6. Stress/Robustness Testing
See how the system handles edge cases.
- **Cases**: Network stream disconnection, low light video, very crowded scenes (many people), empty frames.

## 7. Model Validation (mAP)
If you train your own models, you should test their accuracy on a labeled dataset.
- **Tool**: YOLOv8 validation scripts (`yolo val model=yolov8n.pt data=...`).
