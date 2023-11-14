import streamlit as st
from PIL import Image
import pickle as pkl
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

st.title('Data exploration')

st.header('Upload a dataset')
uploaded_file = st.file_uploader("Choose a .csv file", type=(['csv']))

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    st.header('Show data')
    st.dataframe(df)

    st.header('Describe attributes')
    st.table(df.describe())

    st.header('Show attribute information')
    st.write(df.info(verbose=True))

    st.header('Show correlation between variables')
    st.table(df.corr())

    st.header('Visualize data')
    st.bar_chart(df)
