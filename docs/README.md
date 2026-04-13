# Project Documentation Index

This directory contains detailed technical documents and guides for the AI Violence Detection System.

### 🏠 Main Documentation
For installation, usage, and API reference, please see the [Main README](../README.md).

### 📖 Technical Guides
1. **[Core Architecture](../PROJECT_GUIDE.md)**: Details on internal logic and model handling.
2. **Setup**: Refer to the core requirements in [main README](../README.md#setup-installation).
3. **Training**: For training instructions, refer to `train.py` and the `data/` organization guide.

---

## Technical Summary
- **Backend**: FastAPI (Python 3.10)
- **AI Models**: YOLOv8n (Detection) + YOLOv8n-cls (Classification)
- **Logic**: Symmetrical Heuristics for Weapon-Proximity and Rapid Movement.
- **Inference Wrapper**: [model_wrapper.py](../model_wrapper.py)
