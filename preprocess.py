import numpy as np
import cv2
img_width = 256
img_height = 256

def preprocess_img(img):
    img = cv2.resize(img, (img_width, img_height)) 
    img = np.array(img)
    img = np.stack((img,) * 3, axis=-1)
    img = img/img.max()
    img = img.astype(np.float32)
    return img

    
    

