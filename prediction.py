import streamlit as st
import pandas as pd
import numpy as np
import pickle
import json

#Load All files
#Load model

with open('cat_col.txt', 'r') as file_1:
  cat_col = json.load(file_1)

with open('num_col.txt', 'r') as file_2:
  num_col = json.load(file_2)

with open('model_rf.pkl', 'rb') as file_3:
  model_rf = pickle.load(file_3)


def run():
    with st.form('Please fill the form below'):
        # Setup Streamlit interface
        host_id = st.number_input('Host ID', min_value=1, value=4000, format='%d')
        neighbourhood_group = st.selectbox('Neighbourhood Group', options=['Bronx', 'Brooklyn', 'Manhattan', 'Queens', 'Staten Island'])
        neighbourhood = st.text_input('Neighbourhood', value='Upper West Side')
        latitude = st.number_input('Latitude', value=40.82085)
        longitude = st.number_input('Longitude', value=-73.94025)
        room_type = st.selectbox('Room Type', options=['Entire home/apt', 'Private room', 'Shared room'])
        minimum_nights = st.number_input('Minimum Nights', min_value=1, value=1, format='%d')
        number_of_reviews = st.number_input('Number of Reviews', min_value=0, value=0, format='%d')
        reviews_per_month = st.number_input('Reviews per Month', min_value=0.0, value=0.0)
        calculated_host_listings_count = st.number_input('Calculated Host Listings Count', min_value=1, value=2, format='%d')
        availability_365 = st.number_input('Availability 365', min_value=0, value=163, format='%d')

        submitted = st.form_submit_button("Predict Price")

        
    data_inf = {
        'host_id': [host_id],
        'neighbourhood_group': [neighbourhood_group],
        'neighbourhood': [neighbourhood],
        'latitude': [latitude],
        'longitude': [longitude],
        'room_type': [room_type],
        'minimum_nights': [minimum_nights],
        'number_of_reviews': [number_of_reviews],
        'reviews_per_month': [reviews_per_month],
        'calculated_host_listings_count': [calculated_host_listings_count],
        'availability_365': [availability_365]
    }
    data_inf = pd.DataFrame([data_inf])
    st.dataframe(data_inf)

    if submitted:
        #split between numerical and categorical columns
        data_inf_num = data_inf[num_col]
        data_inf_cat = data_inf[cat_col]

        #concate
        data_inf_final = np.concatenate([data_inf_num, data_inf_cat], axis = 1)

        #predict using log reg model

        y_pred_inf = model_rf.predict(data_inf_final)

        st.write('## Predicted Price: $', str(int(y_pred_inf[0])))


if __name__ == '__main__':
   run()    