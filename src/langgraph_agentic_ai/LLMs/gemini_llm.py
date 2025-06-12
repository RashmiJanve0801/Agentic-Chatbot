import os
import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI

class GeminiLLM:
    def __init__(self, user_controls_input):
        self.user_controls_input = user_controls_input

    def get_llm_model(self):
        try: 
            google_api_key = self.user_controls_input['GOOGLE_API_KEY']
            selected_gemini_model = self.user_controls_input['selected_gemini_model']
            if google_api_key =='' and os.environ['GOOGLE_API_KEY'] =='':
                st.error("Please enter the Google API key")

            llm = ChatGoogleGenerativeAI(api_key = google_api_key, model = selected_gemini_model)

        except Exception as e:
            raise ValueError(f"Error occurred with Exception : {e}")

        return llm

