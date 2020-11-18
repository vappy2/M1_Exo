import os
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import seaborn as sns

st.title('Visualisation des données')

st.subheader('Choissisez un tableau de données')

# method for dataset files selector
def file_selector(folder_path='./dataset'):
    # list files name on folder_path
    filenames = os.listdir(folder_path)
    # select specific dataset from list
    selected_filename = st.selectbox('Select a dataset',filenames)
    # return the path / file
    return os.path.join(folder_path,selected_filename)

# define filename as current file selected
filename = file_selector()
# display filename selected
st.info('Dataset selected {}'.format(filename))

# Read Dataset
df = pd.read_csv(filename)
