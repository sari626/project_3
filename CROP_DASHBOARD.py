import streamlit as st
import pandas as pd
import joblib

# Load model and dataset
model = joblib.load('rf_crop_model.pkl')
df = pd.read_csv('cleaned_faostat.csv')

st.title("🌾 Crop Production Prediction App")

# Inputs
area = st.selectbox("Select Area", sorted(df['Area'].unique()))
crop = st.selectbox("Select Crop", sorted(df['Item'].unique()))
year = st.slider("Select Year", int(df['Year'].min()), int(df['Year'].max()))
area_harvested = st.number_input("Area Harvested (ha)", min_value=0.0)
yield_val = st.number_input("Yield (kg/ha)", min_value=0.0)

# Predict button
if st.button("Predict Production"):
    input_data = pd.DataFrame([[area, crop, year, area_harvested, yield_val]],
                              columns=['Area', 'Item', 'Year', 'Area_harvested', 'Yield'])

    # Encode
    input_encoded = pd.get_dummies(input_data)
    for col in model.feature_names_in_:
        if col not in input_encoded.columns:
            input_encoded[col] = 0
    input_encoded = input_encoded[model.feature_names_in_]

    # Prediction
    prediction = model.predict(input_encoded)[0]
    st.success(f"Predicted Crop Production: {round(prediction)} tons")
