import streamlit as st
import numpy as np
from PIL import Image
from tensorflow import keras

model = keras.models.load_model('model.keras')

st.title('Kedi mi Köpek mi? :dog:')

dosya = st.file_uploader('Bir fotoğraf yükleyin', type=['jpg', 'jpeg', 'png'])

if dosya is not None:
    resim = Image.open(dosya).convert('RGB')
    st.image(resim, width=300)
    x = np.array(resim.resize((160, 160)), dtype=np.float32)[np.newaxis]
    p = float(model.predict(x)[0][0])
    if p > 0.5:
        st.success(f'Köpek 🐶 (olasılık: %{p * 100:.1f})')
    else:
        st.success(f'Kedi 🐱 (olasılık: %{(1 - p) * 100:.1f})')