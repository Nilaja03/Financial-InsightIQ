import pandas as pd
import numpy as np
import pickle as pkl
import streamlit as st

def main():
    model = pkl.load(open('C:/Users/Nilanjana/Documents/2021-2025/2022-2025 KSIT/KSIT/2nd to 4th year (2022-2025)/3rd Year (2023-2024)/6th Sem/7) Mini Project/project/Medical_Insurance_Premium_Prediction_Model.pkl', 'rb'))

    st.header('Medical Insurance Premium Predictor')

    gender = st.selectbox('Choose your Gender:',['Female','Male'])
    smoker = st.selectbox('Are you a smoker?',['Yes','No'])
    region = st.selectbox('Which region are you from?',['South-East','South-West','North-East','North-West'])
    age = st.slider('What is your Age?',5,80)
    bmi = st.slider('What is the BMI value?',5,100)
    children = st.slider('How many children do you have?',0,5)


    if gender == 'Female':
        gender = 0
    else:
        gender = 1

    if smoker == 'No':
        smoker = 0
    else:
        smoker = 1

    if region == 'South-East':
        region = 0
    if region == 'South-West':
        region = 1
    if region == 'North-East':
        region = 2
    else:
        region = 3


    input_data = (age, gender, bmi, children, smoker, region)
    input_data = np.asarray(input_data)
    input_data = input_data.reshape(1,-1)

    if st.button('Predict'):
        predicted_prem = model.predict(input_data)
        predicted_prem_in_rupee = round(predicted_prem[0] * 83.49)
        st.write(f'You can avail a medical insurance premium of ₹{predicted_prem_in_rupee}')