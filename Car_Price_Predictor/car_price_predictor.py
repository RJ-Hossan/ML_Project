# -*- coding: utf-8 -*-
"""
Created on Fri Nov 24 22:57:41 2023

@author: mdref
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu


# loading the saved models

car_price_model = pickle.load(open('C:/Users/mdref/Downloads/ML_Project/Car_Price_Predictor/car_price.sav', 'rb'))


# sidebar for navigation
with st.sidebar:
    
    selected = option_menu('Car Price Predictor',
                          
                          ['Car Price Prediction'],
                          icons=['car'],
                          default_index=0)
    
if (selected == 'Car Price Prediction'):
    
    # page title
    st.title('Car Price Prediction Using ML')
    
    
    # getting the input data from the user
    col1, col2, col3 = st.columns(3)
    
    with col1:
        Year = st.text_input('Year of Buying the Car')
        
    with col2:
        Present_Price = st.text_input('Present Price of the Car')
    
    with col1:
        Kms_Driven = st.text_input('Total Driven (Kms)')
    
    with col2:
        Fuel_Type = st.text_input('Fuel Type [0-Petrol; 1-Diesel; 2-CNG]')
    
    with col1:
        Seller_Type = st.text_input('Seller Type [0-Dealer; 1-Individual]')
    
    with col2:
        Transmission = st.text_input('Transmission[0-Manual; 1-Automated]')
    
    with col2:
        Owner = 0
    
    
# code for Prediction
car_price = ''

# creating a button for Prediction
if st.button('Car Price Predict'):
    # Make the prediction
    car_price_prediction = car_price_model.predict([[Year, Present_Price, Kms_Driven, Fuel_Type, Seller_Type, Transmission, Owner]])
    
    # Update the car_price variable with the predicted value
    car_price = f'Predicted Car Price: {car_price_prediction[0]}'

# Display the result
st.success(car_price)
