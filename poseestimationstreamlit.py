import streamlit as st
import cv2
import mediapipe as mp
import numpy as np
from PIL import Image


st.title("Pose Estimation with MediaPipe")
st.text("Upload an image to estimate human pose")
img_file = st.file_uploader("Upload Image", type=["jpg", "jpeg", "png"])


if img_file:
    image = np.array(Image.open(img_file))
else:
    st.warning("Please upload an image.")
    st.stop()

st.subheader("Original Image")
st.image(image, caption="Uploaded Image", use_column_width=True)


def detect_pose(frame):
    mp_pose = mp.solutions.pose
    mp_drawing = mp.solutions.drawing_utils
    pose = mp_pose.Pose(static_image_mode=True, min_detection_confidence=0.5)
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = pose.process(frame_rgb)
    
    if results.pose_landmarks:
        annotated_frame = frame.copy()
        mp_drawing.draw_landmarks(
            annotated_frame, results.pose_landmarks, mp_pose.POSE_CONNECTIONS,
            mp_drawing.DrawingSpec(color=(0, 255, 0), thickness=2, circle_radius=2),
            mp_drawing.DrawingSpec(color=(0, 0, 255), thickness=2, circle_radius=2)
        )
        return annotated_frame
    return frame


pose_image = detect_pose(image)
st.subheader("Pose Estimation Result")
st.image(pose_image, caption="Pose Detected", use_column_width=True)
