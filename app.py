import streamlit as st
import requests


st.title('Diamond App')



def get_predictions(carat_weight, cut, color, clarity, polish, symmetry, report):
    url = 'https://diamoapi.herokuapp.com/predict?carat_weight={carat_weight}&cut={cut}&color={color}&clarity={clarity}&polish={polish}&symmetry={symmetry}&report={report}' \
        .format(carat_weight=carat_weight, cut=cut, \
                color=color, clarity=clarity, polish=polish, symmetry=symmetry, report=report)
    response = requests.post(url)
    json_response = response.json()
    price=json_response['prediction']
    return price





carat_weight = st.number_input("Enter carat weight ")
cut= st.text_input("cut")
color= st.text_input("color")
clarity= st.text_input("clarity")
polish= st.text_input("polish")
symmetry= st.text_input("symmetry")
report= st.text_input("report")





result = ""

# when 'Predict' is clicked, make the prediction and store it
if st.button("Predict"):
    result= get_predictions(carat_weight=carat_weight, cut=cut, color=color, clarity=clarity, polish=polish,symmetry=symmetry, report=report)
    st.success(f'Price of Diamond  {result}')