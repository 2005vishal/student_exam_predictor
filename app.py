import streamlit as st
import pandas as pd
import pickle
import numpy as np

@st.cache_resource
def load_all_data():
    with open('student_model_v2.pkl', 'rb') as f:
        return pickle.load(f)


saved_data = load_all_data()
model = saved_data["model"]
encoders = saved_data["encoders"]

st.title("🎓 Student Performance Predictor By Vishal Patwa")


col1, col2,col3, col4 = st.columns(4)

with col1:
    study_hours = st.number_input("Study Hours", 0.0, 10.0, 4.0)
    attendance = st.slider("Attendance (%)", 0, 100, 80)
    sleep_hours = st.number_input("Sleep Hours", 0.0, 12.0, 7.0)


with col2:

    gender = st.selectbox("Gender", encoders['gender'].classes_)
    course = st.selectbox("Course", encoders['course'].classes_)
    internet = st.selectbox("Internet Access", encoders['internet_access'].classes_)
with col4:
    sleep_qual = st.selectbox("Sleep Quality", encoders['sleep_quality'].classes_)
    age = st.number_input("Age", 15, 30, 20)
with col3:
    method = st.selectbox("Study Method", encoders['study_method'].classes_)
    facility = st.selectbox("Facility Rating", encoders['facility_rating'].classes_)
    difficulty = st.selectbox("Exam Difficulty", encoders['exam_difficulty'].classes_)

if st.button("Predict Score"):

    input_dict = {
        'age': age,
        'gender': encoders['gender'].transform([gender])[0],
        'course': encoders['course'].transform([course])[0],
        'study_hours': study_hours,
        'class_attendance': attendance,
        'internet_access': encoders['internet_access'].transform([internet])[0],
        'sleep_hours': sleep_hours,
        'sleep_quality': encoders['sleep_quality'].transform([sleep_qual])[0],
        'study_method': encoders['study_method'].transform([method])[0],
        'facility_rating': encoders['facility_rating'].transform([facility])[0],
        'exam_difficulty': encoders['exam_difficulty'].transform([difficulty])[0]
    }

    input_df = pd.DataFrame([input_dict])

    # Predict
    prediction = model.predict(input_df)[0]
    st.success(f"### Predicted Exam Score: {prediction:.2f}")