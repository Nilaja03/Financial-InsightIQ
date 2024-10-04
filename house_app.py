import pandas as pd
import pickle as pk
import streamlit as st

def main():
    model = pk.load(open('C:/Users/Nilanjana/Documents/2021-2025/2022-2025 KSIT/KSIT/2nd to 4th year (2022-2025)/3rd Year (2023-2024)/6th Sem/7) Mini Project/project/House_Price_Prediction_Model.pkl','rb'))

    st.header('Bangalore House Prices Predictor')
    data = pd.read_csv('C:/Users/Nilanjana/Documents/2021-2025/2022-2025 KSIT/KSIT/2nd to 4th year (2022-2025)/3rd Year (2023-2024)/6th Sem/7) Mini Project/project/Cleaned_House_Data.csv')

    loc = st.selectbox('Where would you want to live?', data['location'].unique())
    sqft = st.number_input('How big a house would you want? (total sqft)')
    beds = st.number_input('How many bedrooms would you like?')
    bath = st.number_input('How many bathrooms would you like?')
    balc = st.number_input('How many balconies would you like?')

    input = pd.DataFrame([[loc,sqft,bath,balc,beds]], columns=['location','total_sqft','bath','balcony','bedrooms'])

    if st.button("Predict House Price"):
        output = model.predict(input)
        predicted_price = round(output[0] * 100000)
        st.write(f'Price of the House can be around ₹{predicted_price}')