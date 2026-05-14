import streamlit as st
import cv2
import av
import time

from streamlit_webrtc import (
    webrtc_streamer,
    VideoProcessorBase
)

st.title("AI-Based Posture Correction System")

face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades +
    "haarcascade_frontalface_default.xml"
)


class PostureProcessor(VideoProcessorBase):

    def __init__(self):

        self.baseline_width = None
        self.baseline_y = None

        self.score = 100

        self.bad_posture_start = 0

    def recv(self, frame):

        img = frame.to_ndarray(format="bgr24")

        gray = cv2.cvtColor(
            img,
            cv2.COLOR_BGR2GRAY
        )

        faces = face_cascade.detectMultiScale(
            gray,
            1.1,
            5
        )

        posture_text = "NO FACE DETECTED"

        color = (0, 255, 0)

        current_time = time.time()

        for (x, y, w, h) in faces:

            cv2.rectangle(
                img,
                (x, y),
                (x + w, y + h),
                (255, 0, 0),
                2
            )

            # Initial calibration
            if self.baseline_width is None:

                self.baseline_width = w
                self.baseline_y = y

            width_threshold = (
                self.baseline_width * 1.15
            )

            y_threshold = (
                self.baseline_y + 25
            )

            bad_posture = False

            # Leaning too close
            if w > width_threshold:

                posture_text = (
                    "BAD POSTURE"
                )

                bad_posture = True

            # Looking down
            elif y > y_threshold:

                posture_text = (
                    "LOOK UP"
                )

                bad_posture = True

            else:

                posture_text = (
                    "GOOD POSTURE"
                )

            # Bad posture timer
            if bad_posture:

                color = (0, 0, 255)

                if self.bad_posture_start == 0:

                    self.bad_posture_start = (
                        current_time
                    )

                elapsed = (
                    current_time -
                    self.bad_posture_start
                )

                if elapsed > 2:

                    self.score -= 1

                    self.score = max(
                        self.score,
                        0
                    )

            else:

                self.bad_posture_start = 0

                if self.score < 100:

                    self.score += 1

            # Posture text
            cv2.putText(
                img,
                posture_text,
                (40, 50),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                color,
                3
            )

            # Score
            cv2.putText(
                img,
                f"Score: {self.score}",
                (40, 100),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.8,
                (255, 255, 255),
                2
            )

            # Warning
            if bad_posture and elapsed > 2:

                cv2.putText(
                    img,
                    "PLEASE SIT STRAIGHT",
                    (40, 150),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.8,
                    (0, 0, 255),
                    3
                )

        return av.VideoFrame.from_ndarray(
            img,
            format="bgr24"
        )


webrtc_streamer(
    key="posture",
    video_processor_factory=PostureProcessor,
    media_stream_constraints={
        "video": True,
        "audio": False
    },
    rtc_configuration={
        "iceServers": [
            {
                "urls": [
                    "stun:stun.l.google.com:19302"
                ]
            }
        ]
    }
)
