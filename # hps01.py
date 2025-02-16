# hps01.py
# Helper script for pose estimation preprocessing

import numpy as np

def preprocess_image(image):
    """Resize and normalize image for model input."""
    image = cv2.resize(image, (256, 256))
    image = image.astype(np.float32) / 255.0
    image = np.expand_dims(image, axis=0)
    return image


def postprocess_results(results):
    """Convert model output to readable keypoints."""
    keypoints = np.squeeze(results)
    return [(int(x), int(y)) for x, y in keypoints]
