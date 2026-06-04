import streamlit as st
import pandas as pd
import pickle
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
MODEL_PATH = BASE_DIR / "models" / "churn_model.pkl"

with open(MODEL_PATH, "rb") as file:
    model = pickle.load(file)


st.set_page_config(
    page_title="Customer Churn Prediction",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Customer Churn Prediction")
st.write(
    "Predict whether a customer is likely to churn based on account information."
)


col1, col2 = st.columns(2)

with col1:
    tenure = st.slider(
        "Tenure (Months)",
        0,
        72,
        12
    )

    monthly_charges = st.number_input(
        "Monthly Charges",
        min_value=0.0,
        value=70.0
    )

    total_charges = st.number_input(
        "Total Charges",
        min_value=0.0,
        value=1000.0
    )

    senior = st.selectbox(
        "Senior Citizen",
        ["No", "Yes"]
    )

    gender = st.selectbox(
        "Gender",
        ["Female", "Male"]
    )

with col2:

    contract = st.selectbox(
        "Contract Type",
        [
            "Month-to-month",
            "One year",
            "Two year"
        ]
    )

    internet = st.selectbox(
        "Internet Service",
        [
            "DSL",
            "Fiber optic",
            "No"
        ]
    )

    paperless = st.selectbox(
        "Paperless Billing",
        ["No", "Yes"]
    )

    tech_support = st.selectbox(
        "Tech Support",
        ["No", "Yes"]
    )

    online_security = st.selectbox(
        "Online Security",
        ["No", "Yes"]
    )

if st.button("Predict"):

    data = {
        'SeniorCitizen': 0,
        'tenure': tenure,
        'MonthlyCharges': monthly_charges,
        'TotalCharges': total_charges,
        'gender_Male': 0,
        'Partner_Yes': 0,
        'Dependents_Yes': 0,
        'PhoneService_Yes': 1,
        'MultipleLines_No phone service': 0,
        'MultipleLines_Yes': 0,
        'InternetService_Fiber optic': 0,
        'InternetService_No': 0,
        'OnlineSecurity_No internet service': 0,
        'OnlineSecurity_Yes': 0,
        'OnlineBackup_No internet service': 0,
        'OnlineBackup_Yes': 0,
        'DeviceProtection_No internet service': 0,
        'DeviceProtection_Yes': 0,
        'TechSupport_No internet service': 0,
        'TechSupport_Yes': 0,
        'StreamingTV_No internet service': 0,
        'StreamingTV_Yes': 0,
        'StreamingMovies_No internet service': 0,
        'StreamingMovies_Yes': 0,
        'Contract_One year': 0,
        'Contract_Two year': 0,
        'PaperlessBilling_Yes': 0,
        'PaymentMethod_Credit card (automatic)': 0,
        'PaymentMethod_Electronic check': 1,
        'PaymentMethod_Mailed check': 0
    }

    # Senior Citizen
    if senior == "Yes":
        data['SeniorCitizen'] = 1

    # Gender
    if gender == "Male":
        data['gender_Male'] = 1

    # Contract
    if contract == "One year":
        data['Contract_One year'] = 1

    elif contract == "Two year":
        data['Contract_Two year'] = 1

    # Internet
    if internet == "Fiber optic":
        data['InternetService_Fiber optic'] = 1

    elif internet == "No":
        data['InternetService_No'] = 1

    # Paperless
    if paperless == "Yes":
        data['PaperlessBilling_Yes'] = 1

    # Tech Support
    if tech_support == "Yes":
        data['TechSupport_Yes'] = 1

    # Online Security
    if online_security == "Yes":
        data['OnlineSecurity_Yes'] = 1

    input_df = pd.DataFrame([data])

    prediction = model.predict(input_df)[0]

    probability = model.predict_proba(input_df)[0][1]

    st.divider()

    st.subheader("Prediction Result")

    if prediction == 1:
        st.error(
            f"⚠️ Customer is likely to churn\n\nProbability: {probability:.2%}"
        )
    else:
        st.success(
            f"✅ Customer is likely to stay\n\nProbability of churn: {probability:.2%}"
        )