import streamlit as st
import pandas as pd
import joblib

st.title("House Price Prediction App")

uploaded_file = st.file_uploader("Upload your house features CSV file", type=["csv"])

if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)
    st.write("Preview of uploaded data:", data.head())

    # Load the saved model pipeline
    model = joblib.load('xgb_house_price_model.pkl')

    # Predict house prices
    predictions = model.predict(data)

    # Show predictions
    st.write("Predicted House Prices:")
    st.write(predictions)

    # Visualize predictions as a bar chart
    st.bar_chart(predictions)

else:
    st.info("Please upload a CSV file to get house price predictions.")
