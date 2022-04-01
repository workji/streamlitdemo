import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time


st.title('Streamlit Sample')
st.write('progressbar')

'Start!!!'
latest_interaction = st.empty()
bar1 = st.progress(0)

for i in range(100):
    latest_interaction.text(f'Iteration {i+1}')
    bar1.progress(i + 1)
    time.sleep(0.1)

'Done!!!'


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




