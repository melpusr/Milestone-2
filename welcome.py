import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px 
from PIL import Image 

def run(): 
    #membuat judul
    st.title('New York Airbnb Listing')

    #sub header
    st.subheader('Airbnb around New York (2019)')

    #tambah gambar
    image = Image.open('airbnb.jpg')
    st.image(image, caption = 'Airbnb is one of the convenient applications to help you search suitable abode.')

    #font size
    st.write('### Welcome!')
    st.write('##### Do you want to search a place that suits your needs and taste, but tight on budget? Worry not. With this website we tried to help in adjusting your budget.')

    #membuat batas dengan garis lurus
    st.markdown('---')

    #show dataframe
    data = pd.read_csv('AB_NYC_2019.csv')

    #membuat histogram berdasarkan input user
    st.write('### Show data')
    option = st.selectbox('Choose data: ', ('neighbourhood_group', 'room_type'))
    fig = plt.figure(figsize = (15,5))
    sns.countplot(x=data[option])
    plt.xticks(rotation=90)  
    st.pyplot(fig)

    st.write('### Distribution of Availability by Neighbourhood Group')
    fig, ax = plt.subplots(figsize=(10, 10))  
    sns.boxplot(data=data, x='neighbourhood_group', y='availability_365', hue='neighbourhood_group', palette='plasma', legend=False)
    st.pyplot(fig)


    st.markdown('---')
    st.write('**Page dibuat oleh Amelia P.S. untuk Milestone 2 Hacktiv8 FTDS batch RMT-30**')

if __name__=='__main__':
    run()