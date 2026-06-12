# ❤️ Heart Disease Prediction using Machine Learning

A simple Machine Learning project that predicts the likelihood of heart disease based on patient health metrics.

https://heart-disease-prediction-123456.streamlit.app/

## Project Goal

The primary goal of this project was to learn and practice the complete Machine Learning workflow:

* Data Cleaning
* Exploratory Data Analysis (EDA)
* Handling Missing Values and Duplicates
* Feature Encoding
* Feature Scaling
* Model Training
* Model Evaluation
* Model Deployment

This project was created as a learning exercise while studying Machine Learning concepts.

## Dataset

The project uses a Heart Disease dataset containing medical attributes such as:

* Age
* Sex
* Resting Blood Pressure
* Cholesterol
* Fasting Blood Sugar
* Maximum Heart Rate
* Exercise-Induced Angina
* Oldpeak
* Number of Major Vessels
* Chest Pain Type
* ECG Results
* Slope
* Thalassemia

Target:

* `0` = No Heart Disease
* `1` = Heart Disease Present

## Machine Learning Workflow

### Data Preprocessing

* Removed duplicate rows
* One-Hot Encoded categorical features
* Standard Scaled numerical features
* Split data into training and testing sets

### Models Tested

* Logistic Regression
* K-Nearest Neighbors (KNN)
* Decision Tree
* Support Vector Machine (SVM)

### Evaluation Metrics

Models were evaluated using:

* Accuracy
* Precision
* Recall
* F1-Score
* Classification Report

## Deployment

The trained model was deployed using Streamlit to provide an interactive web interface for predictions.

## Running the Project

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
streamlit run app.py
```

## Technologies Used

* Python
* Pandas
* NumPy
* Scikit-Learn
* Joblib
* Streamlit

## Note

The Machine Learning workflow, preprocessing, model training, evaluation, and overall project implementation were completed as part of my learning process.

The Streamlit user interface code was generated with the assistance of AI tools to help create a simple frontend quickly, allowing me to focus primarily on learning Machine Learning concepts rather than frontend development.

## Author

Bhavik Vavadiya

B.Tech Computer Science Engineering Student
