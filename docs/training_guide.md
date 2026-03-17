# AI Detection - Training Setup Guide

To train a YOLOv8 model for violence detection, you need to organize your data correctly. Depending on how you want to detect violence, there are two main approaches:

## 1. Classification (Simplest)
If you just want the model to say "Violent" or "Normal" for an entire image/frame.

### Folder Structure
Organize your `data/` folder like this:
```text
data/
  train/
    violence/
      img1.jpg
    "non-violence"/
      img2.jpg
  val/
    violence/
      img3.jpg
    "non-violence"/
      img4.jpg
```
**Usage**: You can train this by running `python train.py --task classify`.

## 2. Object Detection (Advanced)
If you want the model to draw boxes around "violent acts" (e.g., a person punching another). This requires labeled data.

### Folder Structure
```text
data/
  images/
    train/
      img1.jpg
    val/
      img2.jpg
  labels/
    train/
      img1.txt  (YOLO format labels)
    val/
      img2.txt
```

### `data.yaml`
You must provide a `data.yaml` file that looks like this:
```yaml
path: ./data
train: images/train
val: images/val

names:
  0: "non-violence"
  1: violence
```
**Usage**: You can train this by running `python train.py --task detect`.

## Recommended Approach

## Using Kaggle Video Data
If you have a dataset from Kaggle, I have optimized the extraction script to handle it automatically.

### 1. Organize your Videos
Place your Kaggle folders inside the `videos/` directory. The script handles common Kaggle folder names and maps them to your preferred names (`voilence` and `non-voilence`).
```text
videos/
  voilence/
    V_1.mp4
  "non voilence"/
    NV_1.mp4
```

### 2. Run the Extraction Script
This script will **automatically split** your data into 80% Training and 20% Validation sets.
```powershell
.\venv\Scripts\python.exe extract_frames.py --interval 10 --split 0.8
```

### 3. Start Training
Once the script finishes, your `data/` folder will be organized as:
- `data/train/voilence/`
- `data/train/non-voilence/`
- `data/val/voilence/`
- `data/val/non-voilence/`

You can then start training:
```powershell
.\venv\Scripts\python.exe train.py --task classify
```
