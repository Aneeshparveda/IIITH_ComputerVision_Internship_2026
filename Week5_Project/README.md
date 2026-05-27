
# Week 5 – ECIS Project

# ECIS – Electronic Component Intelligence System

## Overview

ECIS is a computer vision based inspection system designed for intelligent analysis of electronic components and PCB defects using deep learning and image processing techniques.

The project combines:
- object detection,
- OCR,
- defect analysis,
- and component classification
into a unified AI workflow.

---

## Features

- Electronic component detection using YOLO
- OCR-based part number extraction
- PCB defect inspection
- Basic anomaly detection
- Automated visual analysis pipeline

---

## Example PCB Defects

The following image shows common PCB manufacturing defects used in computer vision inspection systems.

![PCB Defects](pcb_defects.png)

---

## Defect Types

- Missing Hole
- Mouse Bite
- Open Circuit
- Short Circuit
- Spur
- Spurious Copper

---

## Workflow

```text
Input PCB Image
      ↓
Component Detection
      ↓
OCR Extraction
      ↓
Defect Detection
      ↓
Final Inspection Output
```

---

## Technologies Used

- Python
- OpenCV
- Ultralytics YOLO
- EasyOCR
- NumPy

---

## Future Scope

- Real-time PCB inspection
- Embedded deployment
- Industrial automation
- Streamlit dashboard integration
- Advanced anomaly detection
