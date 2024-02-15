# -*- coding: utf-8 -*-


import pickle
import streamlit as st
from streamlit_option_menu import option_menu

from PIL import Image

icon = Image.open('page_icon.png')
st.set_page_config(
        page_title="Multiple Disease Prediction",
        page_icon=icon,
        layout="wide"
)


#loading the saved models
diabetes_model = pickle.load(open('diabetes_model.sav', 'rb'))

heart_disease_model = pickle.load(open('heart_disease_model.sav', 'rb'))

parkinsons_model = pickle.load(open('parkinsons_model.sav', 'rb'))

kidney_disease_model = pickle.load(open('kidney_model.sav', 'rb'))


#sidebar for navigation
with st.sidebar:
    select = option_menu('Diseases Prediction',
                         
                         ['Diabetes Prediction',
                          'Heart Disease Prediction',
                          'Parkinsons Disease Prediction',
                          'Kidney Disease Prediction'],
                         
                         icons = ['activity', 'heart', 'person', ''],
                         
                         default_index = 0)
    

#Diabetes prediction page
if select == 'Diabetes Prediction':
    #page title
    st.title('Diabetes Prediction')
    
    #columns for input fields
    col1, col2, col3 = st.columns(3)
    
    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')
    with col2:
        Glucose = st.text_input('Glucose Level')
    with col3:
        BloodPressure = st.text_input('Blood Pressure Value')
    with col1:
        SkinThickness = st.text_input('Skin Thickness Value')
    with col2:
        Insulin = st.text_input('Insulin Level')
    with col3:
        BMI = st.text_input('BMI Value')
    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function Value')
    with col2:
        Age = st.text_input('Age')
    
    #code for Prediction
    diabetes_diagnosis = ''
    
    #button for prediction
    if st.button('Diabetes Test Result'):
        diabetes_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
        
        if diabetes_prediction[0]==0:
            diabetes_diagnosis = 'The person is Not Diabetic'
        else:
            diabetes_diagnosis = 'The person is Diabetic'
            
    st.success(diabetes_diagnosis)
    

#Heart Disease prediction page
if select == 'Heart Disease Prediction':
    #page title
    st.title('Heart Disease Prediction')
    
    #columns for input fields
    col1, col2, col3 = st.columns(3)
    
    with col1:
        age = st.text_input('Age')
    with col2:
        sex=0
        display = ("Select", "Male", "Female")
        options = list(range(len(display)))
        value = st.selectbox("Gender", options, format_func=lambda x: display[x])
        if value == "Male":
            sex = 1
        elif value == "Female":
            sex = 0
        
    with col3:
        cp=0
        display = ("Select", "Typical Angina", "Atypical Angina", "Non-Anginal Pain", "Asymptotic")
        options = list(range(len(display)))
        value = st.selectbox("Chest_Pain Type", options, format_func=lambda x: display[x])
        if value == "Typical Angina":
            cp = 0
        elif value == "Atypical Angina":
            cp = 1
        elif value == "Non-Anginal Pain":
            cp = 2
        elif value == "Asymptotic":
            cp = 3
        
    with col1:
        trestbps = st.text_input('Resting Blood Pressure')
    with col2:
        chol = st.text_input('Serum Cholestrol in mg/dL')
    with col3:
        fbs = st.text_input('Fasting Blood Sugar > 120 mg/dL')
    with col1:
        restecg = st.text_input('Resting Electrocardiographic results')
    with col2:
        thalach = st.text_input('Maximum Heart Rate achieved')
    with col3:
        exang = st.text_input('Exercise Induced Angina')
    with col1:
        oldpeak = st.text_input('ST depression induced by exercise')
    with col2:
        slope = st.text_input('Slope of the peak exercise ST segment')
    with col3:
        ca = st.text_input('Major vessels colored by flourosopy')
    with col1:
        thal = st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')
    
    
    #code for Prediction
    heart_disease_diagnosis = ''
    
    #button for prediction
    if st.button('Heart Disease Test Result'):
        heart_disease_prediction = heart_disease_model.predict([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])
        
        if heart_disease_prediction[0]==0:
            heart_disease_diagnosis = 'The person does Not Have Heart Disesase'
        else:
            heart_disease_diagnosis = 'The person Has Heart Disease'
            
    st.success(heart_disease_diagnosis)
    
    
#Parkinson's prediction page
if select == 'Parkinsons Disease Prediction':
    #page title
    st.title('Parkinsons Disease Prediction')
    
    #columns for input fields
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        fo = st.text_input('MDVP: Fo(Hz)')
    with col2:
        fhi = st.text_input('MDVP: Fhi(Hz)')
    with col3:
        flo = st.text_input('MDVP: Flo(Hz)')
    with col4:
        jitter_percent = st.text_input('MDVP: Jitter(%)')
    with col1:
        jitter_abs = st.text_input('MDVP: Jitter(Abs)')
    with col2:
        rap = st.text_input('MDVP: RAP')
    with col3:
        ppq = st.text_input('MDVP: PPQ')
    with col4:
        ddp = st.text_input('Jitter: DDP')
    with col1:
        shimmer = st.text_input('MDVP: Shimmer')
    with col2:
        shimmer_db = st.text_input('MDVP: Shimmer(dB)')
    with col3:
        shimmer_apq3 = st.text_input('Shimmer: APQ3')
    with col4:
        shimmer_apq5 = st.text_input('Shimmer: APQ5')
    with col1:
        apq = st.text_input('MDVP: APQ')
    with col2:
        dda = st.text_input('MDVP: DDA') 
    with col3:
        nhr = st.text_input('NHR')
    with col4:
        hnr = st.text_input('HNR')
    with col1:
        RPDE = st.text_input('RPDE')
    with col2:
        DFA = st.text_input('DFA')
    with col3:
        spread1 = st.text_input('spread1')
    with col4:
        spread2 = st.text_input('spread2')
    with col1:
        d2 = st.text_input('D2')
    with col2:
        ppe = st.text_input('PPE')
    
    #code for Prediction
    parkinsons_diagnosis = ''
    
    #button for prediction
    if st.button('Parkinsons Disease Test Result'):
        parkinsons_prediction = parkinsons_model.predict([[fo, fhi, flo, jitter_percent, jitter_abs, rap, ppq, ddp, shimmer, shimmer_db, shimmer_apq3, shimmer_apq5, apq, dda, nhr, hnr, RPDE, DFA, spread1, spread2, d2, ppe]])
        
        if parkinsons_prediction[0]==0:
            parkinsons_diagnosis = 'The person does Not Have Parkinsons Disease'
        else:
            parkinsons_diagnosis = 'The person Has Parkinsons Disease'
            
    st.success(parkinsons_diagnosis)
    
#Kidney Disease prediction page
if select == 'Kidney Disease Prediction':
    #page title
    st.title('Kidney Disease Prediction')
    
    #columns for input fields
    col1, col2, col3 = st.columns(3)
    

    
    with col1:
        age = st.text_input('Age')
    with col2:
        bp = st.text_input('Blood Pressure') 
    with col3:
        sg = st.text_input('Specific Gravity')        
    with col1:
        al = st.text_input('Albumin')
    with col2:
        su = st.text_input('Sugar Level')
    with col3:
        rbc = st.text_input('Red Blood Cells')
    with col1:
        pc = st.text_input('Pus Cells')
    with col2:
        pcc = st.text_input('Pus Cell Clumps')
    with col3:
        ba = st.text_input('Bacteria')
    with col1:
        bgr = st.text_input('Blood Glucose Random')
    with col2:
        bu = st.text_input('Blood Urea')
    with col3:
        sc = st.text_input('Serum Creatinine')        
    with col1:
        sod = st.text_input('Sodium')
    with col2:
        pot = st.text_input('Potassium')
    with col3:
        hemo = st.text_input('Hemoglobin')
    with col1:
        pcv = st.text_input('Packed Cell Volume')
    with col2:
        wc = st.text_input('White Blood Cell Count')
    with col3:
        rc = st.text_input('Red Blood Cell Count')
    with col1:
        htn = st.text_input('Hypertension')
    with col2:
        dm = st.text_input('Diabetes Mellitus')
    with col3:
        cad = st.text_input('Coronary Artery Disease')
    with col1:
        appet = st.text_input('Appetite')        
    with col2:
        pe = st.text_input('Pedal Edema')
    with col3:
        ane = st.text_input('Anemia')
    
    
    
    #code for Prediction
    kidney_diagnosis = ''
    
    #button for prediction
    if st.button('Kidney Disease Test Result'):
        kidney_prediction = kidney_disease_model.predict([[age, bp, sg, al, su, rbc, pc, pcc, ba, bgr, bu, sc, sod, pot, hemo, pcv, wc, rc, htn, dm, cad, appet, pe, ane]])
        
        if kidney_prediction[0]==0:
            kidney_diagnosis = 'The person does Not Have Kidney Disease'
        else:
            kidney_diagnosis = 'The person Has Kidney Disease'
            
    st.success(kidney_diagnosis)


    



    
    
    
    
    
    
    
    
    
    
