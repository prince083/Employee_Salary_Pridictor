import streamlit as st
import pandas as pd
import joblib

# Load the trained model
model = joblib.load("best_model.pkl")

st.set_page_config(page_title="Employee Salary Classification💰", page_icon="🪙", layout="centered")

# Enhanced CSS with improved contrast and visibility
st.markdown("""
    <style>
        body, .stApp {
            background-color: #FFF2E0;
            color: #3c3c3c;
        }

        h1, h2, h3, h4, h5, h6, p {
            color: #3c3c3c;
        }

        .css-1d391kg, .css-1avcm0n {
            background-color: #C0C9EE !important;
        }

        .stSidebar {
            background-color: #C0C9EE;
            color: #292929;
        }

        .stButton>button {
            background-color: #898AC4 !important;
            color: white;
            font-weight: bold;
            border-radius: 8px;
            font-size: 16px;
        }

        .stButton>button:hover {
            background-color: #6d6fb0 !important;
        }

        .stDownloadButton>button {
            background-color: #A2AADB;
            color: white;
            font-weight: bold;
        }

        .css-1v0mbdj {
            color: #292929;
        }

        .stDataFrame {
            background-color: white;
        }

        .block-container {
            padding-top: 2rem;
        }

        .css-1v3fvcr {
            background-color: #FFF2E0;
        }
    </style>
""", unsafe_allow_html=True)

# Main Title
st.title("Employee Salary Classifier")
st.markdown("<p style='text-align: center;'>Predict if an employee earns more than 50K or not based on their profile details.</p>", unsafe_allow_html=True)
st.markdown("---")

# Sidebar Inputs
st.sidebar.header("Input Employee Details")

age = st.sidebar.slider("Age", 18, 65, 30)
education = st.sidebar.selectbox("🎓 Education Level", [
    "Bachelors", "Masters", "PhD", "HS-grad", "Assoc", "Some-college"
])
occupation = st.sidebar.selectbox("💼 Job Role", [
    "Tech-support", "Craft-repair", "Other-service", "Sales",
    "Exec-managerial", "Prof-specialty", "Handlers-cleaners", "Machine-op-inspct",
    "Adm-clerical", "Farming-fishing", "Transport-moving", "Priv-house-serv",
    "Protective-serv", "Armed-Forces"
])
hours_per_week = st.sidebar.slider("⏱️ Hours per week", 1, 80, 40)
gender = st.sidebar.selectbox("🚻 Gender", ["male", "female"])

# Input DataFrame
input_df = pd.DataFrame({
    'age': [age],
    'education': [education],
    'occupation': [occupation],
    'hours-per-week': [hours_per_week],
    'gender': [gender]
})

# Preview Data
st.subheader("👀 Preview Input Data")
st.dataframe(input_df)

# Prediction
if st.button("🚀 Predict Salary Class"):
    prediction = model.predict(input_df)
    result = "Earns >50K" if prediction[0] == '>50K' else "Earns ≤50K"
    color = "#4CAF50" if prediction[0] == '>50K' else "#FF5722"
    st.markdown(f"<h3 style='color:{color}'>✅ Prediction: {result}</h3>", unsafe_allow_html=True)
    #st.success(f"✅ Prediction: {prediction[0]}")

# Batch Prediction
st.markdown("---")
st.markdown("#### 📂 Batch Prediction")
uploaded_file = st.file_uploader("Upload a CSV file for batch prediction", type="csv")

if uploaded_file is not None:
    batch_data = pd.read_csv(uploaded_file)
    st.write("Uploaded data preview:", batch_data.head())
    batch_preds = model.predict(batch_data)
    batch_data['PredictedClass'] = batch_preds
    st.write("✅ Predictions:")
    st.dataframe(batch_data)
    csv = batch_data.to_csv(index=False).encode('utf-8')
    st.download_button("Download Predictions CSV", csv, file_name='predicted_classes.csv', mime='text/csv')
