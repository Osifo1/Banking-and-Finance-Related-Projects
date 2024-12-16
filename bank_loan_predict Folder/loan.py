import streamlit as st
import pandas as pd
import joblib
import numpy as np

# Load the saved model
model = joblib.load('loan_prediction_model.pkl')

# Function to make predictions
def predict_loan_status(gender, married, education, self_employed, applicant_income, coapplicant_income, loan_amount, loan_amount_term, credit_history, dependents):
    # Create a DataFrame for the input features
    input_data = pd.DataFrame({
        'Gender': [1 if gender == 'Male' else 0],
        'Married': [1 if married == 'Yes' else 0],
        'Education': [1 if education == 'Graduate' else 0],
        'Self_Employed': [1 if self_employed == 'Yes' else 0],
        'ApplicantIncome': [applicant_income],
        'CoapplicantIncome': [coapplicant_income],
        'LoanAmount': [loan_amount],
        'Loan_Amount_Term': [loan_amount_term],
        'Credit_History': [1.0 if credit_history == "1.0" else 0.0],
        'Dependents_1': [1 if dependents == '1' else (0 if dependents == '0' else (0 if dependents == '2' else 0))],
        'Dependents_2': [1 if dependents == '2' else (0 if dependents == '0' else (0 if dependents == '1' else 0))],
        'Dependents_3+': [1 if dependents == '3+' else (0 if dependents in ['0', '1', '2'] else 0)],
        'Property_Area_Semiurban': [0],
        'Property_Area_Urban': [0]
    })

    # Make predictions
    prediction = model.predict(input_data)

    return prediction[0]

# Title of the app
st.title("3MTT Knowledge Showcase on Bank's Loan Prediction App")

# Input fields
gender = st.selectbox("Gender", ["Male", "Female"])
married = st.selectbox("Married", ["Yes", "No"])
education = st.selectbox("Education", ["Graduate", "Not Graduate"])
self_employed = st.selectbox("Self Employed", ["Yes", "No"])
applicant_income = st.number_input("Applicant Income", min_value=0)
coapplicant_income = st.number_input("Coapplicant Income", min_value=0)
loan_amount = st.number_input("Loan Amount", min_value=0)
loan_amount_term = st.number_input("Loan Amount Term (months)", min_value=0)
credit_history = st.selectbox("Credit History", ["1.0", "0.0"])
dependents = st.selectbox("Dependents", ["0", "1", "2", "3+"])

if st.button("Predict"):
    result = predict_loan_status(gender, married, education, self_employed, applicant_income, coapplicant_income, loan_amount, loan_amount_term, credit_history, dependents)
    st.success(f"The predicted Loan Status is: {'Approved' if result == 0 else 'Not Approved'}")
