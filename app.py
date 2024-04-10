import streamlit as st
import os
import cv2
import random
import numpy as np
import pandas as pd 
from io import BytesIO
import tensorflow as tf
import pydicom as dicom
from tensorflow import keras
from keras.models import load_model 
from keras import backend as K
import matplotlib.pyplot as plt
os.environ["SM_FRAMEWORK"] = "tf.keras"
import segmentation_models as sm
from segmentation_models import Unet,get_preprocessing
from keras.utils import plot_model
from keras.callbacks import EarlyStopping ,ReduceLROnPlateau ,ModelCheckpoint

st.title("Efficient UNet Model in Action")

sm.set_framework('tf.keras')
sm.framework()
BACKBONE = 'efficientnetb2'
preprocess_input = get_preprocessing(BACKBONE)
model = Unet(BACKBONE, encoder_weights='imagenet')
model.compile(optimizer='adam', loss=sm.losses.DiceLoss(), metrics=[tf.keras.metrics.Recall(),
                                    tf.keras.metrics.Precision(),
                                    tf.keras.metrics.AUC(),
                                    sm.metrics.iou_score,
                                    sm.metrics.FScore(threshold=0.5)])

model.load_weights('/home/lokeswarlakhineni/codespace/lung Nodule segmentation using Res Unet/archived_weights/model_1.weights.h5')




def predict(image):
    img = cv2.resize(image,(256, 256)) 
    img = np.array(img)
    img = img/img.max()
    img = img.astype(np.float32)
    img = img.reshape(1,img.shape[0],img.shape[1],img.shape[2])
    prediction = model.predict(img)
    return prediction

uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    file_bytes = uploaded_file.read()
    nparr = np.frombuffer(file_bytes, np.uint8)
    image = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    col1, col2 = st.columns(2)
    st.image(image, caption='Image', use_column_width=True)
    if st.button('Start Prediction'):
        prediction = predict(image)
        st.image(prediction, caption='Image', use_column_width=True)