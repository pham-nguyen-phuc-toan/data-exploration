import streamlit as st
from PIL import Image
import pickle as pkl
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

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
    st.write(df.info())

    st.header('Show correlation between variables')
    fig, ax = plt.subplots()
    sns.heatmap(df.corr(method='pearson'), ax=ax, vmax=1,square=True,annot=True,cmap='Reds')
    st.write(fig)
    
    st.header('Visualize data')
    for col in df.columns:
        st.bar_chart(pd.DataFrame(df[col]), x=col)
