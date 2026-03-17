# AI Violence & Weapon Detection System

This is a real-time AI detection module for detecting violence and weapons from video streams (webcam, video files, RTSP).

## Prerequisites
- **Python:** Strictly `3.10.x`
- **OS:** Windows / Linux / macOS

## Setup & Installation

### 1. Create a Virtual Environment
We strongly recommend creating a virtual environment to avoid dependency conflicts.
```bash
python -m venv venv
```

### 2. Activate the Environment
- **Windows:**
  ```bash
  .\venv\Scripts\activate
  ```
- **macOS/Linux:**
  ```bash
  source venv/bin/activate
  ```

### 3. Install Dependencies
There are two ways to install dependencies based on your hardware.

#### Option A: CPU-Only Installation (Default/Safe)
Run the following command to install exactly the versions specified in `requirements.txt`.
```bash
pip install -r requirements.txt
```

#### Option B: GPU (CUDA) Installation
For real-time fast performance with an NVIDIA GPU:
1. First, install PyTorch with CUDA 11.8 or 12.1 support directly from the official PyTorch index (matching the pinned version):
   ```bash
   pip install torch==2.3.1 torchvision==0.18.1 --index-url https://download.pytorch.org/whl/cu118
   ```
2. Then, install the rest of the libraries:
   ```bash
   pip install ultralytics==8.2.0 opencv-python==4.9.0.80 numpy==1.26.4
   ```

### 4. Verify Installation
You can verify the setup by running the Python interpreter:
```bash
python -c "import torch, cv2, ultralytics; print('Setup is Successful!')"
```

## Running the Application
The behavior of the application is controlled via the `MODE` constant in `config/settings.py`.

1. Open `config/settings.py` and set your desired mode:
   - `MODE = "webcam"` (Primary - uses default system camera)
   - `MODE = "video"` (Set `VIDEO_FILE_PATH = "test.mp4"`)
   - `MODE = "rtsp"` (Set `RTSP_URL = "rtsp://..."`)
2. Run the main processing script:
   ```bash
   python main.py
   ```
3. Press `q` to safely exit the display window at any time.

## Troubleshooting Common Errors

- **Error: `ModuleNotFoundError: No module named 'cv2'`**
  - Fix: Ensure you activated the virtual environment and successfully installed `opencv-python==4.9.0.80`.
- **Error: Webcam does not open / Frame read failure**
  - Fix: Check if another application (e.g. Teams, Zoom) is currently using your camera. Ensure Windows Privacy Settings allow Apps to access your camera.
- **Error: `RuntimeError: Expected all tensors to be on the same device`**
  - Fix: This often happens if the model is on GPU but the array is on CPU. Our YOLOv8 wrapper inherently manages this by forcing CPU operations when needed, but ensure your PyTorch and Torchvision installations are correctly matched.
- **Error: Low FPS**
  - Fix: Run using the GPU installation option described above, or ensure no other heavy background processes are running. The system inherently uses the lightweight `yolov8n.pt` to mitigate this.
- **Error: Missing `yolov8n.pt` file**
  - Fix: The ultralytics library will automatically download this file internally the first time you run `main.py`. Ensure you have an active internet connection.
