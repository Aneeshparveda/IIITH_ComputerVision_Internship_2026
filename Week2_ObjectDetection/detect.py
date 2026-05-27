from ultralytics import YOLO

# Load pretrained YOLO model
model = YOLO("yolov8n.pt")

# Run object detection on PCB image
results = model(
    "pcb_image.jpg",
    save=True
)

print("PCB Object Detection Completed Successfully")
