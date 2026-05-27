import streamlit as st
import requests
import subprocess
import time


def start_fastapi():

    try:
        # Check if FastAPI already running
        requests.get("http://127.0.0.1:8000/docs")

    except:

        # Start FastAPI server
        subprocess.Popen(
            [
                "uvicorn",
                "api.app:app",
                "--host",
                "127.0.0.1",
                "--port",
                "8000"
            ]
        )

        # Wait for server to start
        time.sleep(5)


# Start FastAPI automatically
start_fastapi()

st.set_page_config(
    page_title="Customer Churn Prediction",
    layout="centered"
)

st.title("Customer Churn Prediction")

st.write("Enter customer details below")

# -----------------------------------------
# CUSTOMER INPUTS
# -----------------------------------------

customer_id = st.number_input("Customer ID", value=1)

gender = st.selectbox(
    "Gender",
    ["Male", "Female"]
)

senior_citizen = st.selectbox(
    "Senior Citizen",
    [0, 1]
)

partner = st.selectbox(
    "Partner",
    ["Yes", "No"]
)

dependents = st.selectbox(
    "Dependents",
    ["Yes", "No"]
)

tenure = st.slider(
    "Tenure",
    0,
    72,
    12
)

phone_service = st.selectbox(
    "Phone Service",
    ["Yes", "No"]
)

multiple_lines = st.selectbox(
    "Multiple Lines",
    ["Yes", "No"]
)

internet_service = st.selectbox(
    "Internet Service",
    ["DSL", "Fiber optic", "No"]
)

online_security = st.selectbox(
    "Online Security",
    ["Yes", "No"]
)

online_backup = st.selectbox(
    "Online Backup",
    ["Yes", "No"]
)

device_protection = st.selectbox(
    "Device Protection",
    ["Yes", "No"]
)

tech_support = st.selectbox(
    "Tech Support",
    ["Yes", "No"]
)

streaming_tv = st.selectbox(
    "Streaming TV",
    ["Yes", "No"]
)

streaming_movies = st.selectbox(
    "Streaming Movies",
    ["Yes", "No"]
)

contract_type = st.selectbox(
    "Contract Type",
    [
        "Month-to-month",
        "One year",
        "Two year"
    ]
)

payment_method = st.selectbox(
    "Payment Method",
    [
        "Electronic check",
        "Mailed check",
        "Bank transfer (automatic)",
        "Credit card (automatic)"
    ]
)

monthly_charges = st.number_input(
    "Monthly Charges",
    value=70.0
)

total_charges = st.number_input(
    "Total Charges",
    value=1000.0
)

# -----------------------------------------
# PREDICT BUTTON
# -----------------------------------------

if st.button("Predict Churn"):

    payload = {

        "id": customer_id,
        "gender": gender,
        "senior_citizen": senior_citizen,
        "partner": partner,
        "dependents": dependents,
        "tenure": tenure,
        "phone_service": phone_service,
        "multiple_lines": multiple_lines,
        "internet_service": internet_service,
        "online_security": online_security,
        "online_backup": online_backup,
        "device_protection": device_protection,
        "tech_support": tech_support,
        "streaming_tv": streaming_tv,
        "streaming_movies": streaming_movies,
        "contract_type": contract_type,
        "payment_method": payment_method,
        "monthly_charges": monthly_charges,
        "total_charges": total_charges
    }

    try:

        response = requests.post(
            "http://127.0.0.1:8000/predict",
            json=payload
        )

        result = response.json()

        churn_probability = result["churn_probability"]

        st.success(
            f"Churn Probability: {churn_probability:.2f}"
        )

        if churn_probability > 0.5:

            st.error(
                "Customer is likely to churn"
            )

        else:

            st.success(
                "Customer is likely to stay"
            )

    except Exception as e:

        st.error(f"Error: {e}")