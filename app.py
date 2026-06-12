import streamlit as st
import pandas as pd
import joblib

# ======================
# Page Config
# ======================

st.set_page_config(
    page_title="Heart Disease Predictor",
    page_icon="❤️",
    layout="wide"
)

# ======================
# Load Model
# ======================

model = joblib.load("Heart_Model.pkl")
scaler = joblib.load("scaler.pkl")

# ======================
# Header
# ======================

st.title("❤️ Heart Disease Prediction")
st.markdown(
    "Enter patient information below and click **Predict**."
)

# ======================
# Inputs
# ======================

col1, col2 = st.columns(2)

with col1:
    age = st.number_input(
        "Age",
        min_value=1,
        max_value=120,
        value=30
    )

    sex = st.selectbox(
        "Sex",
        ["Male", "Female"]
    )

    trestbps = st.number_input(
        "Resting Blood Pressure",
        min_value=80,
        max_value=250,
        value=120
    )

    chol = st.number_input(
        "Cholesterol",
        min_value=100,
        max_value=600,
        value=180
    )

    fbs = st.selectbox(
        "Fasting Blood Sugar > 120",
        ["No", "Yes"]
    )

    thalach = st.number_input(
        "Maximum Heart Rate",
        min_value=60,
        max_value=250,
        value=170
    )

with col2:

    exang = st.selectbox(
        "Exercise Induced Angina",
        ["No", "Yes"]
    )

    oldpeak = st.number_input(
        "Oldpeak",
        min_value=0.0,
        max_value=10.0,
        value=0.0,
        step=0.1
    )

    ca = st.selectbox(
        "Number of Major Vessels",
        [0, 1, 2, 3, 4],
        index=0
    )

    cp = st.selectbox(
        "Chest Pain Type",
        [0, 1, 2, 3],
        index=0
    )

    restecg = st.selectbox(
        "Rest ECG",
        [0, 1, 2],
        index=0
    )

    slope = st.selectbox(
        "Slope",
        [0, 1, 2],
        index=0
    )

    thal = st.selectbox(
        "Thal",
        [0, 1, 2, 3],
        index=1
    )

# ======================
# Convert Inputs
# ======================

sex = 1 if sex == "Male" else 0
fbs = 1 if fbs == "Yes" else 0
exang = 1 if exang == "Yes" else 0

cp_0 = 1 if cp == 0 else 0
cp_1 = 1 if cp == 1 else 0
cp_2 = 1 if cp == 2 else 0
cp_3 = 1 if cp == 3 else 0

restecg_0 = 1 if restecg == 0 else 0
restecg_1 = 1 if restecg == 1 else 0
restecg_2 = 1 if restecg == 2 else 0

slope_0 = 1 if slope == 0 else 0
slope_1 = 1 if slope == 1 else 0
slope_2 = 1 if slope == 2 else 0

thal_0 = 1 if thal == 0 else 0
thal_1 = 1 if thal == 1 else 0
thal_2 = 1 if thal == 2 else 0
thal_3 = 1 if thal == 3 else 0

# ======================
# DataFrame
# ======================

input_df = pd.DataFrame([[
    age, sex, trestbps, chol, fbs,
    thalach, exang, oldpeak, ca,
    cp_0, cp_1, cp_2, cp_3,
    restecg_0, restecg_1, restecg_2,
    slope_0, slope_1, slope_2,
    thal_0, thal_1, thal_2, thal_3
]], columns=[
    'age', 'sex', 'trestbps', 'chol', 'fbs',
    'thalach', 'exang', 'oldpeak', 'ca',
    'cp_0', 'cp_1', 'cp_2', 'cp_3',
    'restecg_0', 'restecg_1', 'restecg_2',
    'slope_0', 'slope_1', 'slope_2',
    'thal_0', 'thal_1', 'thal_2', 'thal_3'
])

# ======================
# Scale
# ======================

numeric_cols = [
    'age',
    'trestbps',
    'chol',
    'thalach',
    'oldpeak',
    'ca'
]

input_df[numeric_cols] = scaler.transform(
    input_df[numeric_cols]
)

# ======================
# Prediction
# ======================

st.divider()

if st.button("🔍 Predict Heart Disease Risk", use_container_width=True):

    prediction = model.predict(input_df)

    if prediction[0] == 1:
        st.error(
            "⚠️ Heart Disease Detected"
        )
    else:
        st.success(
            "✅ No Heart Disease Detected"
        )