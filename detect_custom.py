from ultralytics import YOLO
import cv2
import serial
import time

model = YOLO("runs/detect/train5/weights/best.pt").to("cpu")
print("Model classes:", model.names)

arduino = serial.Serial('COM7', 9600)
time.sleep(2)

cap = cv2.VideoCapture("your_video.mp4")
if not cap.isOpened():
    print("Video not opened")
    exit()

try:
    while True:
        ret, frame = cap.read()
        if not ret or frame is None:
            break

        try:
            results = model(frame, conf=0.15)
        except Exception as e:
            print("⚠️ Inference skipped:", e)
            continue

        annotated = results[0].plot()

        ambulance_detected = False
        for box in results[0].boxes:
            cls_id = int(box.cls[0])
            if results[0].names[cls_id].lower() == "ambulance":
                ambulance_detected = True
                break

        if ambulance_detected:
            arduino.write(b'G')
            print("🚨 Ambulance detected → GREEN")
            time.sleep(0.1)

        cv2.imshow("Ambulance Detection", annotated)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

finally:
    cap.release()
    cv2.destroyAllWindows()
    arduino.close()
    print("Clean shutdown")
