# 🎯 Face Detection and Recognition System

[![Python 3.x](https://img.shields.io/badge/python-3.x-blue.svg)](https://www.python.org/)
[![OpenCV](https://img.shields.io/badge/OpenCV-4.5.0+-green.svg)](https://opencv.org/)
[![MediaPipe](https://img.shields.io/badge/MediaPipe-0.8.0+-orange.svg)](https://mediapipe.dev/)

> 🚀 A powerful Python-based face detection and recognition system that uses cutting-edge computer vision to detect, verify, and track faces in real-time using your camera feed.

---

## ✨ Features

🔍 **Core Capabilities:**
- Real-time face detection powered by MediaPipe
- Smart face verification against reference images
- Live camera feed processing with instant feedback
- Intelligent visual feedback system
- High-confidence detection (0.7 threshold)
- Multi-face detection support

## 🛠️ Prerequisites

Ensure you have these tools installed before starting:

- 🐍 Python 3.x
- 📸 OpenCV (opencv-python)
- 🎯 MediaPipe
- 👤 face_recognition library
- 🔢 NumPy

## 📦 Installation

1️⃣ Clone this repository:
```bash
git clone <repository-url>
cd face-detection-system
```

2️⃣ Install dependencies:
```bash
pip install -r requirements.txt
```

## 🚀 Quick Start

1. Place your reference image in the project directory
2. Launch the system:
   ```bash
   python gender_recognition.py
   ```
3. Enter your name when prompted
4. The magic begins! The system will:
   - 📸 Load your reference image
   - 🎥 Start the camera feed
   - 👁️ Detect faces in real-time
   - 🔄 Compare detected faces with your reference
   - ✅ Show results with color-coded boxes

## 🔧 How It Works

### 🎯 Technology Stack
- 🎥 MediaPipe: Efficient face detection
- 👤 face_recognition: Advanced face encoding & comparison
- 📸 OpenCV: Professional image processing

### 🔄 Process Flow
1. Reference image loading & verification
2. Face encoding extraction
3. Real-time video capture
4. Frame-by-frame face detection
5. Smart face comparison
6. Instant visual feedback

## ⌨️ Controls

- 🔴 Press 'q' to quit
- ⚡ Ctrl+C for emergency stop

## 📋 Dependencies

```plaintext
opencv-python >= 4.5.0
mediapipe >= 0.8.0
numpy >= 1.19.0
face_recognition
```

## 📝 Notes

- 📸 Default camera index: 2
- 🎯 Face detection confidence: 0.7
- 👥 Supports multiple face detection

## 🔍 Troubleshooting

If you encounter issues:

1. 📸 Verify camera connection
2. 🖼️ Ensure reference image has a clear face
3. 📦 Check dependency installation
4. 💡 Ensure proper lighting

---

<div align="center">

🌟 **Star this repository if you find it helpful!** 🌟

</div>
