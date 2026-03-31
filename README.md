# 🚗 AI-Based Driver Drowsiness Detection System

## 📌 Overview

Driver fatigue is one of the leading causes of road accidents worldwide. This project presents a **real-time AI-powered drowsiness detection system** that monitors a driver's facial features using computer vision and triggers alerts when signs of fatigue are detected.

The system uses **Eye Aspect Ratio (EAR)**, **Mouth Aspect Ratio (MAR)**, and facial landmark tracking to identify drowsiness and yawning in real time.

---

## 🎯 Key Features

* 👁️ **Eye Blink Detection (EAR)** – Detects prolonged eye closure
* 😴 **Drowsiness Detection** – Alerts when eyes remain closed for a threshold time
* 😮 **Yawning Detection (MAR)** – Identifies fatigue through mouth movement
* 🔊 **Real-Time Alarm System** – Audio alert to wake the driver
* 📹 **Live Webcam Monitoring** – Continuous real-time tracking
* 📊 **Performance Display** – Shows EAR & MAR values on screen

---

## 🧠 System Architecture

```
Webcam Input  
     ↓  
Face Detection (MediaPipe)  
     ↓  
Facial Landmark Extraction  
     ↓  
Feature Calculation (EAR, MAR)  
     ↓  
Decision Logic (Threshold-Based)  
     ↓  
Alert System (Sound Warning)  
```

---

## 🛠️ Tech Stack

| Category        | Tools Used        |
| --------------- | ----------------- |
| Programming     | Python            |
| Computer Vision | OpenCV, MediaPipe |
| Numerical Ops   | NumPy, SciPy      |
| Alert System    | Pygame            |

---

## 📂 Project Structure

```
drowsiness_detection/
│
├── main.py              # Main application logic
├── utils.py             # EAR & MAR calculations
├── alarm.wav            # Alert sound
├── requirements.txt     # Dependencies
└── README.md            # Project documentation
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone Repository

```bash
git clone https://github.com/your-username/drowsiness_detection.git
cd drowsiness_detection
```

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate   # (Windows)
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Run the Project

```bash
python main.py
```

---

## 📸 Demo / Output

👉 Add screenshots or GIF here

Example:

```
![Demo](demo.png)
```

---

## 🚀 Future Enhancements

* 🧍 Head Pose Estimation (detect nodding)
* 📊 Fatigue Score (continuous monitoring system)
* 🌐 Streamlit Dashboard (visual analytics)
* 📱 Mobile App Integration
* 🤖 LSTM-based Temporal Modeling (AI upgrade)
* ☁️ Cloud Deployment

---

## 📈 Applications

* 🚗 Driver Safety Systems
* 🚛 Fleet Management
* 🏭 Industrial Worker Monitoring
* 🛡️ Surveillance Systems

---

## 💡 Challenges & Learnings

* Real-time processing optimization
* Handling low-light conditions
* Reducing false positives
* Understanding facial landmark geometry

---

## 👨‍💻 Author

**Ishant Singh**

* AIML Student
* Passionate about Computer Vision & AI

---

## ⭐ Show Your Support

If you found this project useful:
⭐ Star the repository
🍴 Fork it
📢 Share it

---

## 📬 Contact

Feel free to connect for collaboration or queries!
