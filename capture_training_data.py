import cv2
import os
import random
import numpy as np
from matplotlib import pyplot as plt
import uuid
import time

def ensure_dir(directory):
    """Ensure the specified directory exists; if not, create it."""
    if not os.path.exists(directory):
        os.makedirs(directory)

IMAGE_PATH = os.path.join('data', 'images')
labels = ['awake', 'drowsy']
num_images = 20

# Ensure label directories exist
for label in labels:
    ensure_dir(os.path.join(IMAGE_PATH, label))

vid = cv2.VideoCapture(0)
for label in labels:
    print(f'Collecting images for {label}')
    time.sleep(5.0)

    for img_num in range(num_images):
        ret, frame = vid.read()
        image_path = os.path.join(IMAGE_PATH, label, label + '.' + str(uuid.uuid1()) + '.jpg')
        cv2.imwrite(image_path, frame)
        cv2.imshow('image', frame)
        time.sleep(2)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

vid.release()
cv2.destroyAllWindows()
