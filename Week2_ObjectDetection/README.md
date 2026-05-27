
# Week 2 – Object Detection

## Overview

This task focused on performing object detection using pretrained YOLO models from the Ultralytics framework.

The workflow included:
- creating a Python virtual environment,
- installing Ultralytics YOLO,
- performing object detection on sample images,
- and generating annotated outputs with bounding boxes.

---

## Tasks Completed

- Created Python virtual environment using `venv`
- Installed Ultralytics YOLO
- Performed object detection using pretrained YOLOv8 model
- Generated annotated detection outputs
- Learned basic AI-based object detection workflow

---

## Tools Used

- Python
- Ultralytics YOLO
- OpenCV
- macOS Terminal

---

## Detection Workflow

```text
Input Image
   ↓
YOLO Object Detection
   ↓
Bounding Box Prediction
   ↓
Annotated Output
```

---

## Sample Detection Script

```python
from ultralytics import YOLO

# Load pretrained model
model = YOLO("yolov8n.pt")

# Run object detection
results = model(
    "https://ultralytics.com/images/bus.jpg",
    save=True
)

print("Object Detection Completed")
```

---

## Output

Successfully performed object detection using YOLOv8 pretrained model and generated annotated prediction outputs.
