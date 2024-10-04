import pickle
import streamlit as st

heart_disease_model = pickle.load(open('heart_disease_model.sav','rb'))
st.title("Heart Disease Prediction")
# feature names ---- age	sex	cp	trestbps	chol	fbs	restecg	thalach	exang	oldpeak	slope	ca	thal
age = st.text_input("Enter your Age")
sex= st.text_input("Gender")
cp = st.text_input("Chest Pain Type")
trestbps = st.text_input("Resting Blood Pressure")
chol = st.text_input("CHOL")
fbs = st.text_input("Fasting Blood Sugar")
restecg = st.text_input("RestECG")
thalach = st.text_input("Maximum Heart Rate Achieved")
exang = st.text_input("Exercise Induced Angina")
oldpeak = st.text_input("OLD PEAK")
slope = st.text_input("Slope")
ca = st.text_input("CA")
thal = st.text_input("Thalassemia")

heart_Disease = ''
if st.button('Heart Disease Test Result'):
    heart_prediction = heart_disease_model.predict([[age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal]])
    if (heart_prediction[0] == 1):
        heart_Disease = 'The Person has Healthy Heart'
    else:
        heart_Disease = 'The Person has UnHealthy Heart'
st.sucess(heart_Disease)
