# Online Summer Internship 2026

## Overview
This repository contains my work from the Online Summer Internship 2026. The project focuses on building a complete computer vision workflow including video processing, object detection, semantic segmentation, dataset preparation, custom model training, and final application development using YOLO and OpenCV.

The internship provided hands-on experience in building AI-based vision systems from scratch, starting from raw video processing to training custom deep learning models for real-world applications.

---

## Week 1 – Video Processing

### Tasks Completed
- Downloaded and processed video datasets
- Extracted image frames from video using FFmpeg
- Reconstructed videos from extracted frames
- Added custom audio tracks to generated videos
- Learned video preprocessing workflow for computer vision pipelines

### Tools Used
- FFmpeg
- macOS Terminal
- yt-dlp

---

## Week 2 – Object Detection

### Tasks Completed
- Created Python virtual environments using `venv`
- Installed and configured Ultralytics YOLO
- Performed object detection using pretrained YOLO models
- Applied detection on custom image datasets
- Generated annotated outputs and converted them into videos

### Tools Used
- Python
- Ultralytics YOLO
- OpenCV

---

## Week 3 – Segmentation & Video Comparison

### Tasks Completed
- Performed semantic segmentation on images
- Generated segmented outputs using YOLO segmentation models
- Created segmented videos from processed frames
- Combined original, object-detected, and segmented videos into a single comparison output

### Concepts Learned
- Semantic Segmentation
- Pixel-wise Classification
- Image Masking
- Video Stacking using FFmpeg

---

## Week 4 – Dataset Preparation

### Tasks Completed
- Explored YOLO dataset structure and metadata files
- Understood YAML configuration files and label formats
- Created custom datasets using Label Studio
- Generated train, validation, and test splits
- Prepared dataset annotations for YOLO training

### Tools Used
- Label Studio
- YOLO Dataset Format
- YAML Configuration

---

## Week 5 – Custom YOLO Training & ECIS

### Tasks Completed
- Annotated custom datasets
- Prepared YOLO label files
- Trained YOLO model on custom datasets
- Tested trained weights on unseen images
- Generated prediction outputs and comparison videos

---

# Final Project

# ECIS – Electronic Component Intelligence System

ECIS is a computer vision system designed for intelligent analysis of electronic components using deep learning and OCR techniques.

The system is capable of:
- Detecting electronic components using YOLO
- Classifying detected components
- Extracting part numbers using OCR
- Performing basic defect analysis
- Generating annotated outputs for inspection

---

## ECIS Workflow

```text
Input Image
   ↓
Component Detection using YOLO
   ↓
OCR Extraction
   ↓
Defect Detection
   ↓
Final Component Analysis
```

---

## Technologies Used

- Python
- FFmpeg
- Ultralytics YOLO
- OpenCV
- EasyOCR
- Label Studio
- NumPy

---

## Repository Structure

```text
IIITH_ComputerVision_Internship_2026/
│
├── Week1_VideoProcessing/
├── Week2_ObjectDetection/
├── Week3_Segmentation/
├── Week4_Dataset/
├── Week5_Project/
│
├── README.md
└── requirements.txt
```

---

## Skills Gained

- Video Processing
- Computer Vision
- Object Detection
- Semantic Segmentation
- Dataset Preparation
- Deep Learning Model Training
- OCR Integration
- AI Workflow Development

---

## Future Scope

- Real-time PCB inspection
- Advanced anomaly detection
- Streamlit-based dashboard
- Embedded AI deployment
- Larger electronic component dataset
- Industrial inspection automation

---

## Summary

This internship helped me understand the complete lifecycle of a computer vision project, including:
- data preprocessing,
- object detection,
- segmentation,
- dataset engineering,
- model training,
- inference generation,
- and AI-based application development.

The experience provided practical exposure to real-world computer vision workflows and strengthened my understanding of deep learning-based visual intelligence systems.
