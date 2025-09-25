💰 Insurance Premium Prediction (Segmented ML)
📌 Project Overview

This project develops a Machine Learning regression pipeline to predict individual insurance premiums (Charges).

A segmentation-first strategy is applied: separate, specialized models are built for distinct customer groups (e.g., Young vs. Rest of Population) to capture cost drivers more effectively than a single general model.

All work is organized into four Jupyter notebooks, covering segmentation, baseline models, and hyperparameter optimization.

🎯 Objectives

🔹 Accurate Estimation → Deliver precise premium predictions (low MAE/MSE).

🔹 Segmentation Analysis → Compare specialized vs. monolithic model performance.

🔹 Hyperparameter Tuning → Use GridSearchCV for optimal parameters in Ridge & Lasso.

🔹 Model Specialization → Export segment-specific models & preprocessing pipelines for deployment.

🛠 Workflow

The pipeline runs separately for Young (<30 yrs) and Rest (≥30 yrs) segments:

1️⃣ Data Segmentation & Preprocessing

Load insurance dataset (features: age, sex, BMI, smoker, etc.).

Split data into Young and Rest segments.

Apply One-Hot Encoding for categorical variables.

Standardize numerical features with Scaling.

2️⃣ Model Training & Selection

Algorithms: Linear Regression, Ridge, Lasso.

GridSearchCV (for _with_gr notebooks) → tune hyperparameters (α for Ridge/Lasso).

Evaluation Metrics:

$R^2$ (Goodness of fit)

MAE (Mean Absolute Error)

RMSE (Root Mean Squared Error)

3️⃣ Model Persistence

Save best-performing models with joblib.

Export scalers + feature list for reproducibility.

📓 Notebook Structure
Notebook File	Segment	Optimization	Final Output
ml_premium_prediction_young.ipynb	Young Applicants	Baseline	Initial Model
ml_premium_prediction_young_with_gr.ipynb	Young Applicants	Optimized (GridSearchCV)	artifacts/model_young.joblib
ml_premium_prediction_rest.ipynb	Rest of Population	Baseline	Initial Model
ml_premium_prediction_rest_with_gr.ipynb	Rest of Population	Optimized (GridSearchCV)	artifacts/model_rest.joblib
📊 Dataset Features
Feature	Description	Impact
age	Age of beneficiary	Key segmentation factor
sex	Gender	Binary predictor
bmi	Body Mass Index	Health risk proxy
children	No. of dependents	Family cost driver
smoker	Smoking status	🚬 Strongest predictor
region	Geographic area	Regional variations
charges	Target Variable	Insurance premium (costs billed)
📦 Requirements

Environment setup:

python 3.x
pandas
numpy
scikit-learn
matplotlib
seaborn
joblib
statsmodels

📌 Results

✔ Segmentation boosted accuracy → Specialized models outperformed a single model.
✔ Ridge & Lasso with GridSearchCV → Achieved higher $R^2$ and lower MAE.
✔ Final Artifacts:

model_young.joblib (Young segment)

model_rest.joblib (Rest segment)

Associated scalers & preprocessing pipelines.

📂 These artifacts enable a robust two-stage deployment strategy for production use.

🔗 Insurance Premium Prediction App:- https://ml-project---insurance-price-predictor.streamlit.app/
