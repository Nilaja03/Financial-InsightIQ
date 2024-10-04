import pandas as pd
import pickle as pk
import streamlit as st

def main():
    model = pk.load(open('C:/Users/Nilanjana/Documents/2021-2025/2022-2025 KSIT/KSIT/2nd to 4th year (2022-2025)/3rd Year (2023-2024)/6th Sem/7) Mini Project/project/Loan_Approval_Prediction_Model.pkl','rb'))
    scaler = pk.load(open('C:/Users/Nilanjana/Documents/2021-2025/2022-2025 KSIT/KSIT/2nd to 4th year (2022-2025)/3rd Year (2023-2024)/6th Sem/7) Mini Project/project/loan_scalar.pkl','rb'))

    st.header('Loan Approval Predictor')

    no_of_dep = st.slider('How many people depend on you? (children, parents, spouse)', 0, 5)
    grad = st.selectbox('Are you a Graduate?', ['Graduated', 'Not Graduated'])
    self_emp = st.selectbox('Are you Self-Employed?', ['Yes', 'No'])
    annual_income = st.slider('What is your Annual Income like?', 0, 10000000)
    loan_amount = st.slider('How much loan are you asking for/did you ask for?', 0, 10000000)
    loan_dur = st.slider('How many years do you want the loan for?', 0, 20)
    cibil = st.slider('What is your CIBIL score? (Find out from UPI payment apps for free)', 0, 1000)
    assets = st.slider('What is your net-worth? (total assests amount)', 0, 10000000)

    if grad == "Graduated":
        grad_s = 1
    else:
        grad_s = 0

    if self_emp == "Yes":
        self_emp_s = 1
    else:
        self_emp_s = 0

    if st.button("Predict Loan Approval"):
        pred_data = pd.DataFrame([[no_of_dep,grad_s,self_emp_s,annual_income,loan_amount,loan_dur,cibil,assets]], columns=['no_of_dependents','education','self_employed','income_annum','loan_amount','loan_term','cibil_score','assets'])
        pred_data = scaler.transform(pred_data)
        predict = model.predict(pred_data)
        if predict[0] == 1:
            st.markdown('Loan will be approved.')
        else:
            st.markdown('Loan will be rejected.')