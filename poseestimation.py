```python
import streamlit as st
import cv2
import numpy as np
import mediapipe as mp
from PIL import Image

st.title("Human Pose Estimation with MediaPipe")
st.text('Upload an image for pose detection')

# File Uploader
img_file_buffer = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

@st.cache_data
def pose_detector(image):
    mp_pose = mp.solutions.pose
    mp_drawing = mp.solutions.drawing_utils
    pose = mp_pose.Pose(static_image_mode=True, min_detection_confidence=0.5)

    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = pose.process(image_rgb)

    if results.pose_landmarks:
        mp_drawing.draw_landmarks(
            image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS,
            mp_drawing.DrawingSpec(color=(0, 255, 0), thickness=2, circle_radius=2),
            mp_drawing.DrawingSpec(color=(0, 0, 255), thickness=2, circle_radius=2)
        )
    return image

if img_file_buffer is not None:
    image = np.array(Image.open(img_file_buffer))
    st.image(image, caption="Uploaded Image", use_column_width=True)
    
    output_image = pose_detector(image)
    st.subheader('Pose Estimation Result')
    st.image(output_image, caption="Pose Detected", use_column_width=True)