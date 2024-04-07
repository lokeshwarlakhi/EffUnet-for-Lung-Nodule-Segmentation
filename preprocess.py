import numpy as np
import cv2


def preprocess(img):
    img = np.array(img)
    img = np.stack((img,) * 3, axis=-1)
