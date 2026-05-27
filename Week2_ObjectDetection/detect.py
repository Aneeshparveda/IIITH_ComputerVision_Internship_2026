from ultralytics import YOLO

# Load pretrained YOLO model
model = YOLO("yolov8n.pt")

# Run object detection
results = model(
    "https://ultralytics.com/images/bus.jpg",
    save=True
)

print("Object Detection Completed")
