from ultralytics import YOLO
import cv2

model = YOLO('yolov8n.pt')

cap = cv2.VideoCapture('your_video.mp4')

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    results = model(frame)
    detections = results[0].boxes.cls.cpu().tolist()
    names = results[0].names

    for cls in detections:
        label = names[int(cls)]
        if 'ambulance' in label.lower():  # Won’t work unless trained custom
            print("🚨 Ambulance Detected!")

    annotated = results[0].plot()
    cv2.imshow("Detection", annotated)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
