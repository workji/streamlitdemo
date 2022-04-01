import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image # 画像表示

st.title('main title')
st.write('main text')

left_column, right_column = st.columns(2)

btn1 = left_column.button('右カラムに文字表示')
if btn1:
    right_column.write('左クリックされた。')
else:
    right_column.write('まだっクリックされていない')

expander1 = st.expander('問合せ一覧')
expander1.write('問合せ１')
expander1.write('問合せ２')
expander1.write('問合せ３')

expander2 = st.expander('問合せ一覧')
expander2.write('問合せ１')




