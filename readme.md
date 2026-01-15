# 🚑 Ambulance Detection & Traffic Signal Control System

This project detects **ambulances in video streams using YOLOv8** and **controls a traffic signal via Arduino** to give priority (GREEN signal) when an ambulance is detected.

The system is designed for **smart traffic management**, helping emergency vehicles pass intersections faster and safer.

---

## 📌 Features

- Real-time ambulance detection using **YOLOv8 (Ultralytics)**
- Supports **custom-trained ambulance detection model**
- Video-based inference (can be extended to live camera)
- Serial communication with **Arduino**
- Automatic **GREEN signal trigger** on ambulance detection
- Clean shutdown and error handling

---

## 🛠️ Tech Stack

### Software
- Python 3.8+
- Ultralytics YOLOv8
- OpenCV
- PySerial

### Hardware
- Arduino (Uno / Nano / Mega)
- Traffic light LEDs or relay module
- USB cable

---

## 📂 Project Structure

```
ambulance-detection/
│
├── runs/detect/train5/weights/best.pt   # Custom trained YOLO model
├── ambulance_detection.py               # Main Python script
├── your_video.mp4                       # Input video
├── README.md                            # Project documentation
```

---

## 🚀 How It Works

1. Video frames are captured using OpenCV.
2. Each frame is passed to a **YOLOv8 custom model** trained to detect ambulances.
3. If an ambulance is detected:
   - A signal (`'G'`) is sent to Arduino via serial communication.
   - Arduino switches the traffic light to **GREEN**.
4. Bounding boxes and labels are displayed in real-time.

---

## 📦 Installation

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/yourusername/ambulance-detection.git
cd ambulance-detection
```

### 2️⃣ Install Dependencies
```bash
pip install ultralytics opencv-python pyserial
```

### 3️⃣ Verify YOLO Installation
```bash
yolo version
```

---

## 🎯 Model Details

- Model: **YOLOv8 (Custom Trained)**
- Class required: `ambulance`
- Confidence threshold: `0.15`

> ⚠️ **Note:** Default YOLOv8 models do NOT include ambulances. You must train a custom dataset.

---

## ▶️ Run the Project

```bash
python ambulance_detection.py
```

Press **Q** to quit.

---

## 🔌 Arduino Setup

### Arduino Logic
- Receives serial input `'G'`
- Turns GREEN light ON
- Other signals can be added (`'R'`, `'Y'`)

### Sample Arduino Pseudocode
```cpp
if (Serial.available()) {
  char cmd = Serial.read();
  if (cmd == 'G') {
    // Turn GREEN light ON
  }
}
```

---

## ⚠️ Common Issues & Fixes

| Issue | Solution |
|------|---------|
| Model not detecting | Ensure custom ambulance class exists |
| COM port error | Check Arduino COM port (e.g., COM7) |
| Video not opening | Verify video path |
| No serial response | Check baud rate (9600) |

---

## 🌱 Future Enhancements

- Live CCTV / IP camera integration
- Multiple vehicle priority handling
- Red-Yellow-Green automation logic
- GPS-based ambulance confirmation
- Cloud-based traffic analytics dashboard

---

## 🧠 Use Cases

- Smart city traffic management
- Emergency vehicle prioritization
- AI-based traffic control systems
- Academic & final-year engineering projects

---

## 👨‍💻 Author

**Divyansh Rai**  
AI • Computer Vision • Smart Systems

---

## 📜 License

This project is for **educational and research purposes**. Feel free to modify and extend.

---

🚦 *Saving lives, one green signal at a time.* 🚑

