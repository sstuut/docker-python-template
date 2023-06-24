import string
import streamlit as st
import pandas as pd
import numpy as np

st.title('Dashboard')
st.write('Test')

data = np.random.randn(3,3)
columns = ['col1','col2','col3']
df = pd.DataFrame(data, columns=columns)
st.dataframe(df)