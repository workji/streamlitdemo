import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image # 画像表示

st.title('Streamlit Test')
st.write('表の表示')

df1 = pd.DataFrame({
    'Col 1': [1,6,3,4],
    'Col 2': [30,10,50,60],
})
# st.write(df) # オプション指定できない
# st.dataframe(df, width=800, height=300) # オプション指定できます。
st.dataframe(df1.style.highlight_max(axis=0), width=800, height=300) # 動的表利用時

st.table(df1.style.highlight_max(axis=0)) # 静的表利用時

st.write('MarkDownの表示')
"""
# MarkDown H1
## MarkDown H2
### MarkDown H3
```python
import streamlit as st
import numpy as np
import pandas as pd
```

```java
public class Hello {
    Hello() {}
}
```

"""
st.write('グラフの表示')
df2 = pd.DataFrame(
    np.random.rand(20,3), # 行数,列数指定
    columns=['Col 1','Col 2','Col 3'] # 列タイトル指定
)
st.dataframe(df2.style.highlight_max(axis=0))
st.line_chart(df2)
st.area_chart(df2)
st.bar_chart(df2)

df3 = pd.DataFrame(
    np.random.rand(100,2)/[50, 50] + [35.69, 139.70],
    columns=['lat', 'lon']
)
st.dataframe(df3)
st.map(df3)

st.write('画像の表示')
img1 = Image.open('cal-202202-p.png')
st.image(img1, caption="test image", use_column_width=True)

