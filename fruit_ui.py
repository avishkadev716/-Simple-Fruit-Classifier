
import streamlit as st
import tensorflow as tf
from tensorflow.keras.preprocessing import image
import numpy as np
from PIL import Image

st.title("🍏 Fruit Freshness Classifier")
st.write("Upload a fruit image and the AI will tell you if it's fresh or rotten.")

model = tf.keras.models.load_model("fruit_model.h5")

uploaded_file = st.file_uploader("Choose a fruit image...", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    img = Image.open(uploaded_file).convert('RGB')
    st.image(img, caption='Uploaded Image', use_column_width=True)

    img = img.resize((150, 150))
    img_array = image.img_to_array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)

    prediction = model.predict(img_array)[0][0]
    label = "Fresh 🍏" if prediction < 0.5 else "Rotten 🍌"
    confidence = (1 - prediction) if prediction < 0.5 else prediction

    st.subheader(f"Prediction: **{label}**")
    st.write(f"Confidence: **{confidence*100:.2f}%**")
