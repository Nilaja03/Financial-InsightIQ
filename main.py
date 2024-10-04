import streamlit as st
from streamlit_option_menu import option_menu
from individual_apps import house_app, car_price_app, medical_insurance_app, loan_app, stocks_app

#sidebar for navigation 
with st.sidebar:
    selected = option_menu('Financial InsightIQ',
                           ['About', 'House Price Prediction', 'Car Price Prediction', 'Loan Approval Prediction', 'Medical Insurance Premium Prediction', 'Stocks Prediction'],
                           icons=['', 'house-fill', 'car-front-fill', 'clipboard-check-fill', 'heart-pulse-fill', 'graph-up-arrow'],
                           default_index=0)

def main():

    if (selected == 'About'):
        st.write('<h1 style="color: #3A5B8B;">Welcome to Financial InsightIQ!</h1>', unsafe_allow_html=True)
        st.write('Unlock the power of data with our suite of predictive tools designed just for you. Whether you’re looking to make informed decisions in real estate, vehicles, health insurance, loans, or investments, we’ve got you covered. Dive in and take control of your financial future today!')
        st.write('The <span style="color: #C71585; font-weight: bold;">House Price Predictor</span> helps you discover the estimated value of your home by inputting key details. This tool empowers you to make smarter decisions in the real estate market.', unsafe_allow_html=True)
        st.write('The <span style="color: #C71585; font-weight: bold;">Car Price Predictor</span> finds out how much your car is really worth based on its make, model, and condition. Use this information to negotiate confidently whether you’re buying or selling.', unsafe_allow_html=True)
        st.write('The <span style="color: #C71585; font-weight: bold;">Medical Insurance Premium Predictor</span> helps you get a clearer picture of your potential insurance costs by entering your health information. This app helps you navigate the often confusing world of medical insurance with ease.', unsafe_allow_html=True)
        st.write('The <span style="color: #C71585; font-weight: bold;">Loan Approval Predictor</span> tells you what loan amounts you may qualify for based on your financial situation. This handy tool is perfect for planning your next big purchase or investment, or even plan your for your aspirations and emergencies.', unsafe_allow_html=True)
        st.write('The <span style="color: #C71585; font-weight: bold;">Stock Price Predictor</span> uncovers insights into future stock prices with our predictive analysis. Whether you’re a seasoned investor or just starting, this app can guide your investment decisions.', unsafe_allow_html=True)
        st.write('<h5 style="color: #3A5B8B;">Please choose an app from the sidebar!!</h5>', unsafe_allow_html=True)
    
    if (selected == 'House Price Prediction'):
        house_app.main()
    if (selected == 'Car Price Prediction'):
        car_price_app.main()
    if (selected == 'Medical Insurance Premium Prediction'):
        medical_insurance_app.main()
    if (selected == 'Loan Approval Prediction'):
        loan_app.main()
    if (selected == 'Stocks Prediction'):
        stocks_app.main()

if __name__ == '__main__':
    main()