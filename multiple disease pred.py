
from email.policy import default
import pickle
from tkinter.messagebox import YES
import streamlit as st
from streamlit_option_menu import option_menu
import streamlit_modal as modal
import streamlit.components.v1 as components


# loading the saved models

diabetes_model = pickle.load(open(r'./savedModels/diabetes_model.sav', 'rb'))

heart_disease_model = pickle.load(open(r'./savedModels/heart_disease_model.sav','rb'))

parkinsons_model = pickle.load(open(r'./savedModels/parkinsons_model.sav', 'rb'))



# sidebar for navigation
with st.sidebar:
    
    selected = option_menu('Multiple Disease Prediction System',
                          
                          ['Diabetes Prediction',
                           'Heart Disease Prediction',
                           'Parkinsons Prediction','Prescription Upload'],
                          icons=['activity','heart','person',],
                          default_index=0)


def clear_text():
    if(selected == "Diabetes Prediction"):
        st.session_state["preg"] = "0"
        st.session_state["bmi"] = "0"
        st.session_state["age"] = "0"
        st.session_state["dpf"] = "0"
        st.session_state["insulin"] = "0"
        st.session_state["gluc"] = "0"
        st.session_state["skinthick"] = "0"
        st.session_state["bp"] = "0"
    
# Diabetes Prediction Page
if (selected == 'Diabetes Prediction'):
    
    # page title
    st.title('Diabetes Prediction using ML')
    
    
    # getting the input data from the user
    col1, col2, col3 = st.columns(3)
    
    with col1:
        Pregnancies = st.text_input('Number of Pregnancies',key="preg",value=0)
        
    with col2:
        Glucose = st.text_input('Glucose Level',key="gluc",value=0)
    
    with col3:
        BloodPressure = st.text_input('Blood Pressure value',key="bp",value=0)
    
    with col1:
        SkinThickness = st.text_input('Skin Thickness value',key="skinthick",value=0)
    
    with col2:
        Insulin = st.text_input('Insulin Level',key="insulin",value=0)
    
    with col3:
        BMI = st.text_input('BMI value',key="bmi",value=0)
    
    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value',key="dpf",value=0)
    
    with col2:
        Age = st.text_input('Age of the Person',key="age",value=0)
    
    
    # code for Prediction
    diab_diagnosis = ''
    
    # creating a button for Prediction
    hospital_search = ""
    col1,col2,col3 = st.columns(3,gap="large")
    with col1:
        if st.button('Diabetes Test Result'):
            if Glucose == "0" or BloodPressure == "0" or SkinThickness == "0" or Insulin == "0" or BMI == "0" or DiabetesPedigreeFunction == "0" or Age == "0":
                st.error("Please enter the value of all fields")
            else:
                diab_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
                
                if (diab_prediction[0] == 1):
                    diab_diagnosis = 'The person is diabetic'
                    hospital_search = "true"
                    st.success(diab_diagnosis)
                else:
                    diab_diagnosis = 'The person is not diabetic'
                    hospital_search = "false"
                    st.success(diab_diagnosis)
    
    with col3:
        st.button("Reset Data",on_click=clear_text)
        

   
    open_modal = st.button("Look For Hospitals ")
    if open_modal:
        modal.open()

    if modal.is_open():
        with modal.container():

            html_string = '''
            <body style = "background-color: black;">
            <h1>HTML string in RED</h1>

            <script language="javascript">
            document.querySelector("h1").style.color = "red";
            </script>
            </body>
            '''
            HtmlFile = open("modal.html", 'r', encoding='utf-8')
        
            
            source_code = HtmlFile.read() 
            components.html(source_code,height=300,scrolling=True)

    if(hospital_search=="true"):
        link = '[Look for Hospitals](http://github.com)'
        st.markdown(link, unsafe_allow_html=True)




# Heart Disease Prediction Page
if (selected == 'Heart Disease Prediction'):
    
    # page title
    st.title('Heart Disease Prediction using ML')
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        age = st.text_input('Age')
        
    with col2:
        sex = st.text_input('Sex')
        
    with col3:
        cp = st.text_input('Chest Pain types')
        
    with col1:
        trestbps = st.text_input('Resting Blood Pressure')
        
    with col2:
        chol = st.text_input('Serum Cholestoral in mg/dl')
        
    with col3:
        fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl')
        
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
        
        
     
     
    # code for Prediction
    heart_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Heart Disease Test Result'):
        heart_prediction = heart_disease_model.predict([[age, sex, cp, trestbps, chol, fbs, restecg,thalach,exang,oldpeak,slope,ca,thal]])                          
        
        if (heart_prediction[0] == 1):
          heart_diagnosis = 'The person is having heart disease'
        else:
          heart_diagnosis = 'The person does not have any heart disease'
        
    st.success(heart_diagnosis)
        
    
    

# Parkinson's Prediction Page
if (selected == "Parkinsons Prediction"):
    
    # page title
    st.title("Parkinson's Disease Prediction using ML")
    
    col1, col2, col3, col4, col5 = st.columns(5)  
    
    with col1:
        fo = st.text_input('MDVP:Fo(Hz)')
        
    with col2:
        fhi = st.text_input('MDVP:Fhi(Hz)')
        
    with col3:
        flo = st.text_input('MDVP:Flo(Hz)')
        
    with col4:
        Jitter_percent = st.text_input('MDVP:Jitter(%)')
        
    with col5:
        Jitter_Abs = st.text_input('MDVP:Jitter(Abs)')
        
    with col1:
        RAP = st.text_input('MDVP:RAP')
        
    with col2:
        PPQ = st.text_input('MDVP:PPQ')
        
    with col3:
        DDP = st.text_input('Jitter:DDP')
        
    with col4:
        Shimmer = st.text_input('MDVP:Shimmer')
        
    with col5:
        Shimmer_dB = st.text_input('MDVP:Shimmer(dB)')
        
    with col1:
        APQ3 = st.text_input('Shimmer:APQ3')
        
    with col2:
        APQ5 = st.text_input('Shimmer:APQ5')
        
    with col3:
        APQ = st.text_input('MDVP:APQ')
        
    with col4:
        DDA = st.text_input('Shimmer:DDA')
        
    with col5:
        NHR = st.text_input('NHR')
        
    with col1:
        HNR = st.text_input('HNR')
        
    with col2:
        RPDE = st.text_input('RPDE')
        
    with col3:
        DFA = st.text_input('DFA')
        
    with col4:
        spread1 = st.text_input('spread1')
        
    with col5:
        spread2 = st.text_input('spread2')
        
    with col1:
        D2 = st.text_input('D2')
        
    with col2:
        PPE = st.text_input('PPE')
        
    
    
    # code for Prediction
    parkinsons_diagnosis = ''
    
    # creating a button for Prediction    
    if st.button("Parkinson's Test Result"):
        parkinsons_prediction = parkinsons_model.predict([[fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ,DDP,Shimmer,Shimmer_dB,APQ3,APQ5,APQ,DDA,NHR,HNR,RPDE,DFA,spread1,spread2,D2,PPE]])                          
        
        if (parkinsons_prediction[0] == 1):
          parkinsons_diagnosis = "The person has Parkinson's disease"
        else:
          parkinsons_diagnosis = "The person does not have Parkinson's disease"
        
    st.success(parkinsons_diagnosis)


if(selected == "Prescription Upload"):

    st.title("Upload your prescription")

    link = '[Click here to upload your prescription and check for medicine](http://127.0.0.1:5500/prescription.html)'
    st.markdown(link, unsafe_allow_html=True)

    HtmlFile = open("prescription.html", 'r', encoding='utf-8')
    source_code = HtmlFile.read() 
    components.html(source_code,width=800,height=600,scrolling=True)
