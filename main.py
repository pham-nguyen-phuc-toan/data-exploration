import streamlit as st
from PIL import Image
import pickle as pkl
import numpy as np
import pandas as pd

st.title('Data exploration')

st.header('Upload a dataset')
uploaded_file = st.file_uploader("Choose a .csv file", type=(['csv;]))

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.dataframe(df)
