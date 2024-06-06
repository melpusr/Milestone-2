import streamlit as st
import welcome
import prediction

page = st.sidebar.selectbox('Choose page: ', ('Welcome', 'Price prediction'))

if page == 'Welcome':
    welcome.run()
else:
    prediction.run