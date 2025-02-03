# Face Detection and Recognition System

A Python-based face detection and recognition system that uses computer vision to detect, verify, and track faces in real-time using your camera feed.

## Features

- Real-time face detection using MediaPipe
- Face verification against a reference image
- Live camera feed processing
- Visual feedback with bounding boxes and labels
- High-confidence face detection (0.7 threshold)
- Support for multiple face detection

## Prerequisites

Before you begin, ensure you have the following installed:
- Python 3.x
- OpenCV (opencv-python)
- MediaPipe
- face_recognition library
- NumPy

## Installation

1. Clone this repository or download the source code
2. Install the required dependencies:
```bash
pip install -r requirements.txt
```

## Usage

1. Place your reference image in the project directory
2. Run the face recognition system:
```bash
python gender_recognition.py
```
3. Enter your name when prompted
4. The system will:
   - Load your reference image
   - Start the camera feed
   - Detect faces in real-time
   - Compare detected faces with your reference image
   - Display results with colored boxes (green for match, red for unknown)

## How It Works

The system uses a combination of technologies:
- MediaPipe for efficient face detection
- face_recognition library for face encoding and comparison
- OpenCV for image processing and display

The process follows these steps:
1. Loads and verifies a reference image
2. Extracts face encoding from the reference image
3. Captures live video feed
4. Detects faces in each frame
5. Compares detected faces with the reference face
6. Provides visual feedback in real-time

## Controls

- Press 'q' to quit the application
- The application can be interrupted with Ctrl+C

## Dependencies

- opencv-python >= 4.5.0
- mediapipe >= 0.8.0
- numpy >= 1.19.0
- face_recognition

## Notes

- The system uses camera index 2 by default
- Face detection confidence threshold is set to 0.7 for accuracy
- The system supports multiple face detection and verification simultaneously

## Troubleshooting

If you encounter issues:
1. Ensure your camera is properly connected and accessible
2. Check if the reference image contains a clearly visible face
3. Verify all dependencies are correctly installed
4. Ensure proper lighting conditions for better face detection
