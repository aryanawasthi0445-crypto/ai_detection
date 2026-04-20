# Graph Report - ai_detection  (2026-04-20)

## Corpus Check
- Large corpus: 5873 files · ~11,609,429 words. Semantic extraction will be expensive (many Claude tokens). Consider running on a subfolder, or use --no-semantic to run AST-only.

## Summary
- 94 nodes · 117 edges · 22 communities detected
- Extraction: 64% EXTRACTED · 36% INFERRED · 0% AMBIGUOUS · INFERRED: 42 edges (avg confidence: 0.74)
- Token cost: 0 input · 0 output

## Community Hubs (Navigation)
- [[_COMMUNITY_Community 0|Community 0]]
- [[_COMMUNITY_Community 1|Community 1]]
- [[_COMMUNITY_Community 2|Community 2]]
- [[_COMMUNITY_Community 3|Community 3]]
- [[_COMMUNITY_Community 4|Community 4]]
- [[_COMMUNITY_Community 5|Community 5]]
- [[_COMMUNITY_Community 6|Community 6]]
- [[_COMMUNITY_Community 7|Community 7]]
- [[_COMMUNITY_Community 8|Community 8]]
- [[_COMMUNITY_Community 9|Community 9]]
- [[_COMMUNITY_Community 10|Community 10]]
- [[_COMMUNITY_Community 11|Community 11]]
- [[_COMMUNITY_Community 12|Community 12]]
- [[_COMMUNITY_Community 13|Community 13]]
- [[_COMMUNITY_Community 14|Community 14]]
- [[_COMMUNITY_Community 15|Community 15]]
- [[_COMMUNITY_Community 16|Community 16]]
- [[_COMMUNITY_Community 17|Community 17]]
- [[_COMMUNITY_Community 18|Community 18]]
- [[_COMMUNITY_Community 19|Community 19]]
- [[_COMMUNITY_Community 20|Community 20]]
- [[_COMMUNITY_Community 21|Community 21]]

## God Nodes (most connected - your core abstractions)
1. `run_webcam_mode()` - 15 edges
2. `ViolenceDetector` - 12 edges
3. `WeaponDetector` - 11 edges
4. `AIInferenceWrapper` - 8 edges
5. `VideoStream` - 8 edges
6. `predict()` - 5 edges
7. `extract_frames()` - 5 edges
8. `YOLODetector` - 5 edges
9. `Base64Request` - 3 edges
10. `Unified wrapper for both Detection and Classification models.     Integrates heu` - 3 edges

## Surprising Connections (you probably didn't know these)
- `Base64Request` --uses--> `AIInferenceWrapper`  [INFERRED]
  ai_detection\api.py → ai_detection\model_wrapper.py
- `run_webcam_mode()` --calls--> `VideoStream`  [INFERRED]
  ai_detection\main.py → ai_detection\utils\video_stream.py
- `run_webcam_mode()` --calls--> `YOLODetector`  [INFERRED]
  ai_detection\main.py → ai_detection\detector\yolo_detector.py
- `run_webcam_mode()` --calls--> `ViolenceDetector`  [INFERRED]
  ai_detection\main.py → ai_detection\detector\violence_detector.py
- `run_webcam_mode()` --calls--> `WeaponDetector`  [INFERRED]
  ai_detection\main.py → ai_detection\detector\weapon_detector.py

## Communities

### Community 0 - "Community 0"
Cohesion: 0.27
Nodes (8): AIInferenceWrapper, Unified wrapper for both Detection and Classification models.     Integrates heu, Processes a single frame:         1. Runs Detection (Persons, Weapons)         2, Pre-heats the models to avoid first-request lag., Analyzes spatio-temporal dynamics of persons to determine violence.     Looks fo, ViolenceDetector, Analyzes YOLO outputs specifically for weapons and their relation to humans., WeaponDetector

### Community 1 - "Community 1"
Cohesion: 0.23
Nodes (9): main(), run_webcam_mode(), test_json_output_generation(), display_alerts(), display_fps(), draw_bbox(), generate_json_output(), Utility class for drawing bounding boxes, text alerts, and outputting JSON logs. (+1 more)

### Community 2 - "Community 2"
Cohesion: 0.18
Nodes (9): Base64Request, predict(), decode_image_base64(), decode_image_bytes(), Decodes a base64 string into an OpenCV image (numpy array)., Decodes raw image bytes into an OpenCV image (numpy array)., Configures standard logging for the application., setup_logging() (+1 more)

### Community 3 - "Community 3"
Cohesion: 0.29
Nodes (7): test_violence_detector_low_proximity_fast_movement(), test_violence_detector_no_persons(), test_weapon_detector_held(), test_weapon_detector_not_held(), _calculate_center(), _calculate_distance(), Checks if a detected weapon is near any detected person.         Returns a list

### Community 4 - "Community 4"
Cohesion: 0.24
Nodes (6): extract_frames(), main(), Extracts frames from a video file at a given interval., main(), Reads a frame from the capture source. Handles stream closure., Releases the camera and destroys windows cleanly.

### Community 5 - "Community 5"
Cohesion: 0.29
Nodes (4): Returns the appropriate OpenCV source string/int based on mode., Initializes the OpenCV VideoCapture object., Robust video capture handler to stream frames from Webcam, Video File, or RTSP., VideoStream

### Community 6 - "Community 6"
Cohesion: 0.33
Nodes (3): Runs inference on a single frame.         Filters and groups detections into Per, Wrapper for Ultralytics YOLOv8. Handles model loading, device selection,     and, YOLODetector

### Community 7 - "Community 7"
Cohesion: 0.5
Nodes (3): _calculate_center(), _calculate_distance(), Determines violence alerts based on multiple variables.

### Community 8 - "Community 8"
Cohesion: 0.67
Nodes (0): 

### Community 9 - "Community 9"
Cohesion: 1.0
Nodes (0): 

### Community 10 - "Community 10"
Cohesion: 1.0
Nodes (0): 

### Community 11 - "Community 11"
Cohesion: 1.0
Nodes (0): 

### Community 12 - "Community 12"
Cohesion: 1.0
Nodes (0): 

### Community 13 - "Community 13"
Cohesion: 1.0
Nodes (1): Calculate the center coordinate of a bounding box.

### Community 14 - "Community 14"
Cohesion: 1.0
Nodes (1): Calculate Euclidean distance between two points.

### Community 15 - "Community 15"
Cohesion: 1.0
Nodes (0): 

### Community 16 - "Community 16"
Cohesion: 1.0
Nodes (0): 

### Community 17 - "Community 17"
Cohesion: 1.0
Nodes (1): Draws a standardized bounding box with label logic.

### Community 18 - "Community 18"
Cohesion: 1.0
Nodes (1): Overlays the FPS counter on the top left corner.

### Community 19 - "Community 19"
Cohesion: 1.0
Nodes (1): Draws high-visibility red alerts for violence or weapons.

### Community 20 - "Community 20"
Cohesion: 1.0
Nodes (1): Formats the current frame detections into the required JSON struct.

### Community 21 - "Community 21"
Cohesion: 1.0
Nodes (0): 

## Knowledge Gaps
- **22 isolated node(s):** `Extracts frames from a video file at a given interval.`, `Analyzes spatio-temporal dynamics of persons to determine violence.     Looks fo`, `Determines violence alerts based on multiple variables.`, `Analyzes YOLO outputs specifically for weapons and their relation to humans.`, `Calculate the center coordinate of a bounding box.` (+17 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **Thin community `Community 9`** (2 nodes): `split_dataset.py`, `split_data()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 10`** (2 nodes): `train.py`, `main()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 11`** (1 nodes): `settings.py`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 12`** (1 nodes): `__init__.py`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 13`** (1 nodes): `Calculate the center coordinate of a bounding box.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 14`** (1 nodes): `Calculate Euclidean distance between two points.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 15`** (1 nodes): `__init__.py`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 16`** (1 nodes): `__init__.py`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 17`** (1 nodes): `Draws a standardized bounding box with label logic.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 18`** (1 nodes): `Overlays the FPS counter on the top left corner.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 19`** (1 nodes): `Draws high-visibility red alerts for violence or weapons.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 20`** (1 nodes): `Formats the current frame detections into the required JSON struct.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 21`** (1 nodes): `__init__.py`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `run_webcam_mode()` connect `Community 1` to `Community 0`, `Community 3`, `Community 4`, `Community 5`, `Community 6`?**
  _High betweenness centrality (0.384) - this node is a cross-community bridge._
- **Why does `ViolenceDetector` connect `Community 0` to `Community 1`, `Community 3`, `Community 7`?**
  _High betweenness centrality (0.165) - this node is a cross-community bridge._
- **Why does `predict()` connect `Community 2` to `Community 0`, `Community 4`?**
  _High betweenness centrality (0.144) - this node is a cross-community bridge._
- **Are the 13 inferred relationships involving `run_webcam_mode()` (e.g. with `.start()` and `VideoStream`) actually correct?**
  _`run_webcam_mode()` has 13 INFERRED edges - model-reasoned connections that need verification._
- **Are the 8 inferred relationships involving `ViolenceDetector` (e.g. with `AIInferenceWrapper` and `Unified wrapper for both Detection and Classification models.     Integrates heu`) actually correct?**
  _`ViolenceDetector` has 8 INFERRED edges - model-reasoned connections that need verification._
- **Are the 8 inferred relationships involving `WeaponDetector` (e.g. with `AIInferenceWrapper` and `Unified wrapper for both Detection and Classification models.     Integrates heu`) actually correct?**
  _`WeaponDetector` has 8 INFERRED edges - model-reasoned connections that need verification._
- **Are the 3 inferred relationships involving `AIInferenceWrapper` (e.g. with `Base64Request` and `ViolenceDetector`) actually correct?**
  _`AIInferenceWrapper` has 3 INFERRED edges - model-reasoned connections that need verification._