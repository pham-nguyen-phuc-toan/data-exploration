import streamlit as st
from PIL import Image
import pickle as pkl
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import io

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
    buffer = io.StringIO()
    df.info(buf=buffer)
    s = buffer.getvalue()
    st.text(s)

    st.header('Visualize data')
    for col in df.columns:
        fig, ax = plt.subplots()
        ax.hist(df[col], bins=20)
        plt.xlabel(col)
        plt.ylabel('Quantity')
        st.pyplot(fig)

    st.header('Show correlation between variables')
    fig, ax = plt.subplots()
    sns.heatmap(df.corr(method='pearson'), ax=ax, vmax=1,square=True,annot=True,cmap='Reds')
    st.write(fig)

    depend_var = st.radio('Choose dependent variable', df.columns)

    for col in df.columns.remove(depend_var):
        st.scatter_chart(pd.DataFrame(df[col], df[depend_var]))
