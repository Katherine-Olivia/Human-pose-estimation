Project: Pose Estimation

This project uses OpenCV and TensorFlow to estimate human poses from images and videos.

Files Overview:

estimation_app.py: Main application to run pose estimation.

graph_opt.pb: Pre-trained model graph.

hps01.py: Helper script for processing.

import cv2.py: Script to test OpenCV installation.

pose_estimation.py: Script for image-based pose estimation.

pose_estimation_Video.py: Script for video-based pose estimation.

requirements.txt: Lists required Python packages.

run.jpg, stand.jpg: Sample images for testing.

Installation:

Install dependencies:

pip install -r requirements.txt

Run the pose estimation script:

python pose_estimation.py

Dependencies:

Python 3.10+

OpenCV

TensorFlow

Usage:

Place your images in the project folder.

Run pose_estimation.py for images.

Run pose_estimation_Video.py for videos.

