
from dotenv import load_dotenv
import streamlit as st
import chain
 
load_dotenv()

def poem_generator_app():
    '''
    Function to generate app 

    Returns:
        response(str)
    '''
    with st.form("poem_generator"):
        topic = st.text_input("Enter a topic to generate a poem")
        submitted = st.form_submit_button("Submit")
        if (submitted):
            response = chain.generate_poem(topic)
            st.info(response)
poem_generator_app()