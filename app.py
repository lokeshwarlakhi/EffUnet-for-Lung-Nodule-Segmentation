import streamlit as st
import tensorflow as tf
from tensorflow.keras.preprocessing import image
import numpy as np
from tensorflow.keras.layers import Layer
# from keras.models import load_model
# import segmentation_models as sm
# from segmentation_models import Unet
# from segmentation_models import get_preprocessing
# from tensorflow.keras.utils import plot_model
# sm.set_framework('tf.keras')
# sm.framework()
# BACKBONE = 'efficientnetb2'

# preprocess_input = get_preprocessing(BACKBONE)
# model = Unet(BACKBONE, encoder_weights='imagenet')

# model = model.load_weights('seg_model.h5')


class FixedDropout(Layer):
    def __init__(self, rate, **kwargs):
        super(FixedDropout, self).__init__(**kwargs)
        self.rate = rate

    def call(self, inputs, training=None):
        if training:
            return tf.nn.dropout(inputs, rate=self.rate)
        return inputs


model = tf.keras.models.load_model('seg_model.h5')




def preprocess_image(img_path, target_size=(256, 256)):
    img = image.load_img(img_path, target_size=target_size)
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0) / 255.0  # Normalize pixel values to [0, 1]
    return img_array

def segment_image(img_array):
    segmentation = model.predict(img_array)
    return segmentation[0, :, :, 0]

def main():
    st.title("CT Scan Nodule Segmentation")

    uploaded_file = st.file_uploader("Choose a CT scan image", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        st.image(uploaded_file, caption="Uploaded Image", use_column_width=True)

        if st.button("Start Segmentation"):
            pass
            # Preprocess the uploaded image
            img_array = preprocess_image(uploaded_file)
            
            # Perform segmentation
            segmentation_result = segment_image(img_array)

            # Display original and segmented images
            st.image([img_array[0], segmentation_result], 
                     caption=["Original Image", "Segmentation Result"], 
                     use_column_width=True, format='png')

            # Provide a description based on your analysis
            st.write("Nodule analysis description goes here.")

if __name__ == "__main__":
    main()