import streamlit as st
import prompter
from utils import common_utils as cu

st.set_page_config(page_title="Genesis")

with st.sidebar:
    st.title("Genesis")
    
    st.subheader('Model Parameters')
    
    temperature = st.sidebar.slider('temperature', min_value=0.01, max_value=5.0, value=0.7, step=0.01)
    top_p = st.sidebar.slider('top_p', min_value=0.01, max_value=1.0, value=0.4, step=0.01)
    top_k = st.sidebar.slider('top_k', min_value=1.0, max_value=48.0, value=32.0, step=0.1)
    max_length = st.sidebar.slider('max_length', min_value=64, max_value=4096, value=2048, step=8)
    

st.image("./assets/logo.svg")
st.subheader("An intelligent test case generator harnessing the power of GenAI")

no_of_cases = st.number_input("Number of Test Cases", min_value=1, max_value=100, value=20, key="cases")
regex = st.text_input("Regex", key="regex")

if 'response' not in st.session_state.keys():
    st.session_state.response = dict()
        
col1, col2 = st.columns([1,1])    

def generate_response():
    with st.spinner("Generating Test Cases"):
        response = prompter.generate(no_of_cases,regex)
        st.session_state.response = response

with col1:
    result = st.button("Generate", on_click=generate_response, use_container_width=True) 
with col2:
    st.button("Reset", use_container_width=True)
            
    
if result:
    st.subheader("Results")
    markdown_results = cu.formatter(st.session_state.response)
    print(markdown_results)
    st.markdown(markdown_results)



    




    

