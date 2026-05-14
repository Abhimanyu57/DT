AI-Based Posture Correction System- 


The AI-Based Posture Correction System is a simple real-time computer vision application that monitors a user’s sitting posture using a webcam. The system is developed using Python, OpenCV, Streamlit, and Streamlit WebRTC.

The application detects the user’s face through the webcam and uses face position and movement to identify poor posture habits such as leaning too close to the screen or bending the neck downward. When bad posture is detected continuously for a certain duration, the system displays warning messages and updates the posture score.

The main objective of the project is to promote posture awareness among students, programmers, office workers, and other computer users who spend long hours in front of screens.

Features-

Real-time webcam monitoring
Face detection using OpenCV
Automatic posture calibration
Detection of bad posture conditions
Live posture score display
Warning messages for incorrect posture
Browser-supported webcam functionality


Technologies Used-

Python
OpenCV
Streamlit
Streamlit WebRTC
NumPy
How the System Works

The webcam continuously captures video frames from the user. OpenCV processes these frames and detects the user’s face. The application stores the user’s normal sitting position during initial calibration.

If the face moves significantly closer to the camera or downward from the calibrated position, the system classifies it as bad posture. If poor posture continues for a few seconds, warning messages are displayed and the posture score decreases gradually.

The system provides live visual feedback directly on the screen.

Applications-

Online learning environments
Office workstations
Programming and development work
Gaming setups
General posture awareness
