import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image # 画像表示

st.title('main title')
st.write('main text')

st.sidebar.title('sidebar title')
st.sidebar.write('sidebar text')

txt = st.sidebar.text_input('あなたの趣味を教えてください。')
condition = st.sidebar.slider('あなたの今の満腹度は？', 0, 10, 5)

'あなたの趣味は:', txt
'あなたの今の満腹度は:', condition