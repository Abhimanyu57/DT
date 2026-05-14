# AI-Based Posture Correction System

## Introduction

The AI-Based Posture Correction System is a real-time computer vision application developed using Python, OpenCV, Streamlit, and Streamlit WebRTC. The system uses a webcam to monitor a user’s sitting posture and provides live feedback whenever poor posture is detected.

The application helps users become more aware of unhealthy posture habits such as leaning too close to the screen or bending the neck downward while working, studying, coding, or gaming.


## Features

- Real-time webcam posture monitoring
- Face detection using OpenCV
- Automatic posture calibration
- Detection of bad posture conditions
- Live posture score display
- Warning alerts for poor posture
- Browser-based webcam functionality
- Lightweight and easy-to-use interface


## Technologies Used

- Python
- OpenCV
- Streamlit
- Streamlit WebRTC
- NumPy


## How the System Works

The webcam continuously captures video frames from the user. OpenCV processes these frames and detects the user’s face in real time.

The application stores the user’s normal sitting position during initial calibration. If the face moves significantly closer to the camera or downward from the calibrated position, the system classifies it as bad posture.

When poor posture continues for a few seconds:
- warning messages are displayed
- the posture score decreases gradually

The system provides live visual feedback directly on the screen.

## Applications

- Online learning environments
- Office workstations
- Programming and development work
- Gaming setups
- General posture awareness


