# Human Pose Estimation using Machine Learning

## 📌 Project Overview
This project implements **Human Pose Estimation** using **OpenCV's Deep Neural Network (DNN)** and **MediaPipe Pose**, leveraging a **pre-trained TensorFlow model** for detecting and analyzing key points in human body motion. The application processes real-time video streams and static images for use cases in **healthcare, sports, and motion tracking**.

## 🎯 Objective
Develop an AI-powered model for **real-time** and **image-based** pose estimation, detecting key body joints efficiently for various applications.

## 🛠️ Tech Stack
- **Programming Language:** Python  
- **Libraries:** OpenCV, TensorFlow, NumPy, Matplotlib, Streamlit, MediaPipe, Pillow  
- **Model:** Pre-trained TensorFlow model (graph_opt.pb) for keypoint detection  

## 📂 Project Structure
```
📁 Human-Pose-Estimation
│── pose_estimation.py             # Pose estimation on static images
│── pose_estimation_Video.py       # Pose estimation from video input
│── estimation_app.py              # Streamlit web app for pose estimation
│── hps01.py                       # Real-time pose estimation with MediaPipe
│── import cv2.py                  # MediaPipe pose estimation on images
│── requirements.txt                # Dependencies for the project
│── graph_opt.pb                    # Pre-trained TensorFlow model
```

## 🚀 Features
- **Real-time Pose Estimation** using a webcam
- **Static Image Analysis** for pose detection
- **Video Processing** for motion tracking
- **Streamlit Web App** for easy interaction
- **MediaPipe & OpenCV DNN** implementations
- **Visualization with Matplotlib**

## 📥 Installation
### 1️⃣ Clone the Repository
```bash
git clone https://github.com/your-username/Human-Pose-Estimation.git
cd Human-Pose-Estimation
```

### 2️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

## 🏃‍♂️ Usage
### ▶️ Running Pose Estimation on Images
```bash
python pose_estimation.py
```

### 🎥 Running Pose Estimation on Video
```bash
python pose_estimation_Video.py
```

### 🌐 Running the Web App (Streamlit)
```bash
streamlit run estimation_app.py
```



