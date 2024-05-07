import os
import pickle
import streamlit as st
from streamlit_option_menu import option_menu



# Set page configuration
st.set_page_config(page_title="Health Assistant",
                   layout="wide",
                   page_icon="🧑‍⚕️")

    
# getting the working directory of the main.py
working_dir = os.path.dirname(os.path.abspath(__file__))

# loading the saved models

diabetes_model = pickle.load(open(f'C:/Users/user/Desktop/Dissertation/diabetes_model.sav', 'rb'))


with st.sidebar:
    selected = option_menu(' Disease Prediction System',

                           ['Diabetes Prediction'],
                           menu_icon='hospital-fill',
                           icons=['person'],
                           default_index=0)




# Sidebar menu
st.sidebar.title("Disease Prediction System")


# Main content

st.title('Diabetes Prediction using ML')

col1, col2, col3 = st.columns(3)
with col1:
    Sex = st.text_input('Gender (male or female)')
    IFCCA1 = st.number_input('IFCCA1 Level')
    OmDiast = st.number_input('OmDiast value')
with col2:
    OmSyst = st.number_input('OmSyst value')
    HDLChol = st.number_input('HDLChol Level')
    Cholest = st.number_input('Cholest value')
with col3:
    BMI = st.number_input('BMI value')

    # code for Prediction
if st.button('Diabetes Test Result'):
    user_input = np.array([IFCCA1, OmDiast, OmSyst, HDLChol, Cholest, BMI])
    user_input = np.append(user_input, 1 if Sex.lower() == 'male' else 0)
    user_input = user_input.reshape(1, -1)
    
    # Make prediction
    diab_prediction = diabetes_model.predict(user_input)
    
    if diab_prediction[0] == 1:
        st.success('The person is diabetic')
    else:
        st.success('The person is not diabetic')
