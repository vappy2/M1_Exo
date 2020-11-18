import os
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import seaborn as sns

st.title('Visualisation des données')

#Upload du CSV
st.subheader('Choissisez un tableau de données')

# Méthode pour le data selector
def file_selector(folder_path=os.path.dirname(os.path.realpath(__file__))+'/dataset'):
    # list files name on folder_path
    filenames = os.listdir(folder_path)
    # select specific dataset from list
    selected_filename = st.selectbox('Sélectionner un dataset',filenames)
    # return the path / file
    return os.path.join(folder_path,selected_filename)

# define filename as current file selected
filename = file_selector()
# display filename selected
st.info('Le dataset suivant à été chargé : {}'.format(filename))

# Read Dataset
data = pd.read_csv(filename)

#Soucis : le .DS Store s'affiche


st.subheader('Etude du dataset')

if st.button("Afficher des lignes du dataset") :
	n = st.number_input('Choissisez le nombre de ligne à afficher',value=5)
	st.dataframe(data.head(n))


if st.checkbox("Afficher les colonnes") :

	#on affiche le nom des colonnes du dataset
	#Attention, on n'utilise pas le .info car il est toujours nul
	st.dataframe(data.columns)

if st.checkbox("Afficher le type des colonnes") :
	st.dataframe(data.dtypes)

if st.checkbox('Show shape'):
    st.text('Nombre de lignes')
    st.write(data.shape[0])
    st.text('Nombre de colonnes')
    st.write(data.shape[1])

if st.checkbox('Statistiques descriptive du dataset'):
	st.write(data.describe())

st.subheader('Les graphiques du dataset')
st.text('La heatmap')

# Heatmap de corrélation 
if st.checkbox("Matrice de corrélation"):
	#corr = data.iloc[:, -15:].corr()
    heatmap = sns.heatmap(data.corr(), vmin=-1, vmax=1, annot=True)
    heatmap.set_title('Heatmap de corrélation', fontdict={'fontsize':12}, pad=12)
    st.write(heatmap)
    st.pyplot()
st.set_option('deprecation.showPyplotGlobalUse', False)

#Parce que c'st rigolo
if st.button("Oh c'est rigolo"):
        st.balloons()
