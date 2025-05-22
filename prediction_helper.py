import pandas as pd
from joblib import load
model_other = load("model_others.joblib")
model_young = load("model_young.joblib")
scaler_others = load("scaler_others.joblib")
scaler_young = load("scaler_young.joblib")


def calculate_normalized_risk_score(medical_history):
    # Define risk scores for each disease
    risk_scores = {
        "diabetes": 6,
        "heart disease": 8,
        "high blood pressure": 6,
        "thyroid": 5,
        "no disease": 0,
        "none": 0
    }

    # Split the medical history into individual diseases
    diseases = medical_history.lower().split(" & ")

    # Calculate the total risk score
    total_risk_score = sum(risk_scores.get(disease, 0) for disease in diseases)

    # Define the known minimum and maximum scores based on your dataset
    min_score = 0  # Minimum possible score
    max_score = 14  # Maximum possible score (e.g., "heart disease" + "high blood pressure")

    # Normalize the total risk score
    if max_score != min_score:
        normalized_risk_score = (total_risk_score - min_score) / (max_score - min_score)
    else:
        normalized_risk_score = 0  # Avoid division by zero if all scores are the same

    return normalized_risk_score



def predict(input_values):
    if input_values["Age"] <= 25:
        prediction = model_young.predict(input_values)
    else:
        prediction = model_other.predict(input_values)
    return int(prediction)