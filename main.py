import streamlit as st
import pandas as pd
from prediction_helper import predict, calculate_normalized_risk_score, scaler_young, scaler_others, model_young, \
    model_other

st.title("Insurance Form")

# Initialize a dictionary to store input values
input_values = {}

# Create four side-by-side columns
col1, col2, col3, col4 = st.columns(4)

# Define options for select boxes
gender_options = ['Male', 'Female']
region_options = ['Northeast', 'Northwest', 'Southeast', 'Southwest']
marital_status_options = ['Unmarried', 'Married']
bmi_category_options = ['Overweight', 'Underweight', 'Normal', 'Obesity']
smoking_status_options = ['Regular', 'No Smoking', 'Occasional']
employment_status_options = ['Self-Employed', 'Freelancer', 'Salaried']
medical_history_options = ['High blood pressure', 'No Disease', 'Diabetes & High blood pressure', 'Diabetes & Heart disease', 'Diabetes', 'Diabetes & Thyroid', 'Heart disease', 'Thyroid', 'High blood pressure & Heart disease']
insurance_plan_options = ['Silver', 'Bronze', 'Gold']
genetical_risk_options = ['Low', 'Medium', 'High']

# Populate the columns with input fields
with col1:
    input_values['Age'] = st.number_input("Age", min_value=0, max_value=120, step=1)
    input_values['Gender'] = st.selectbox("Gender", gender_options)
    input_values['Marital Status'] = st.selectbox("Marital Status", marital_status_options)
    input_values['Number Of Dependants'] = st.number_input("Number Of Dependants", min_value=0, max_value=10, step=1)

with col2:
    input_values['Region'] = st.selectbox("Region", region_options)
    input_values['BMI Category'] = st.selectbox("BMI Category", bmi_category_options)
    input_values['Smoking Status'] = st.selectbox("Smoking Status", smoking_status_options)
    input_values['Genetical Risk'] = st.selectbox("Genetical Risk", genetical_risk_options)

with col3:
    input_values['Employment Status'] = st.selectbox("Employment Status", employment_status_options)
    input_values['Income (Lakhs)'] = st.number_input("Income (Lakhs)", min_value=0.0, step=0.1)
    input_values['Medical History'] = st.selectbox("Medical History", medical_history_options)

with col4:
    input_values['Insurance Plan'] = st.selectbox("Insurance Plan", insurance_plan_options)

def preprocess_input(input_values):
    expected_columns = {
        "Age",
    "Number_Of_Dependants",
    "Income_Level",
    "Income_Lakhs",
    "Insurance_Plan",
    "Annual_Premium_Amount",
    "Genetical_Risk",
    "Normalized_Risk_Score",
    "Gender_Male",
    "Region_Northwest",
    "Region_Southeast",
    "Region_Southwest",
    "Marital_status_Unmarried",
    "BMI_Category_Obesity",
    "BMI_Category_Overweight",
    "BMI_Category_Underweight",
    "Smoking_Status_Occasional",
    "Smoking_Status_Regular",
    "Employment_Status_Salaried",
    "Employment_Status_Self - Employed"
    }
    Insurance_Plan_Encoding = {'Bronze':1,'Silver':2,'Gold':3}
    df = pd.DataFrame(0,columns = expected_columns , index = [0])
    for key, value in input_values.items():
        if key == "Gender" and value == "Male":
            df["Gender_Male"] = 1
        elif key == "Region":
            if value == "Northeast":
                df["Region_Northeast"] = 1
            elif value == "Northwest":
                df["Region_Northwest"] = 1
            elif value == "Southeast":
                df["Region_Southeast"] = 1
            elif value == "Southwest":
                df["Region_Southwest"] = 1
        elif key == "Marital Status" and value == "UnMarried":
            df["Marital_status_Unmarried"] = 1
        elif key == "BMI Category":
            if value == "Obesity":
                df["BMI_Category_Obesity"]=1
            elif value == "Overweight":
                df["BMI_Category_Overweight"] = 1
            elif value == "Underweight":
                df["BMI_Category_Underweight"] = 1
        elif key == "Smoking Status":
            if value == "Regular":
                df["Smoking_Status_Regular"] = 1
            elif value == "No Smoking":
                df["Smoking_Status_Regular"] = 1
            elif value == "Occasional":
                df["Smoking_Status_Regular"] = 1
        elif key == "Employment Status":
            if value == "Self-Employed":
                df["Employment_Status_Self - Employed"] = 1
            elif value == "Self-Employed":
                df["Employment_Status_Salaried"] = 1
        elif key == "Insurance Plan":
            df["Insurance_Plan"] = Insurance_Plan_Encoding.get(value, 1)
        elif key == "Age":
            df["Age"] = 1
        elif key == "Number Of Dependants":
            df["Number_Of_Dependants"] = 1
        elif key == "Income (Lakhs)":
            df["Income_Lakhs"] = value
        elif key == "Genetical Risk":
            df["Genetical_Risk"] = value
    df["Normalized_Risk_Score"] = calculate_normalized_risk_score(input_values["Medical History"])
    df = handle_scaling(input_values["Age"],df)
    return df
def handle_scaling(age,df):
    if age <= 25:
        scaler_object = scaler_young
    else:
        scaler_object = scaler_others

    scaler: scaler_object['scaler']
    Cols_to_scale: scaler_object['cols_to_scale']
    df["Income_Level"] = None
    df[Cols_to_scale] = scaler.transform(df[Cols_to_scale])
    df.drop("Income_Level",axis="columns",inplace = True)
    return df
# Submit button
if st.button("Submit"):
    def predict(input_values):
        prediction = preprocess_input(input_values)
        st.success(f"predicted Premium is:{prediction}")



