import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image # 画像表示

st.title('input')
st.write('Display Image')

# slider 
num = st.slider('あなたのおなかいっぱい度は？', 0, 10, 5)
'あなたのおなかいっぱい度は', num, 'です。'


# text input
txt = st.text_input('あなたの趣味を教えてください。')
'あなたの趣味は', txt, 'です。'

# selectbox sample
option = st.selectbox(
    '好きな数字を選んでください。',
    list(range(1,11))
)
'あなた好きな数字は', option, 'です。'

# checkbox sample
if st.checkbox('Show Image'):
    img = Image.open('cal-202202-p.png')
    st.image(img)
