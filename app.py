import streamlit as st
import pandas as pd
import joblib

model=joblib.load("fraud_detection_pipeline.pkl")
st.title("Fraud Detection Prediction App")
st.markdown("please enter the following details to predict whether the transaction is fraudulent or not")
st.divider()
transaction_type=st.selectbox("Transaction Type",["CASH_OUT","PAYMENT","CASH_IN","TRANSFER","DEPOSIT"])
amount=st.number_input("Amount",min_value=0.0,value=1000.0)
OldbalanceOrg=st.number_input("Old Balance (Sender)",min_value=0.0,value=10000.0)
NewbalanceOrig=st.number_input("New Balance (Sender)",min_value=0.0,value=9000.0)
OldbalanceDest=st.number_input("Old Balance (Receiver)",min_value=0.0,value=0.0)
NewbalanceDest=st.number_input("New Balance (Receiver)",min_value=0.0,value=0.0)

if st.button("Predict"):
    input_data=pd.DataFrame({
        "type":[transaction_type],
        "amount":[amount],
        "oldbalanceOrg":[OldbalanceOrg],
        "newbalanceOrig":[NewbalanceOrig],
        "oldbalanceDest":[OldbalanceDest],
        "newbalanceDest":[NewbalanceDest]
    })
    prediction=model.predict(input_data)
    if prediction[0]==1:
        st.error("The transaction is fraud")
    else:
        st.success("The transaction is not fraud")
