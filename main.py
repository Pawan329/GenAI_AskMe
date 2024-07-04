import streamlit as st
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from dotenv import load_dotenv
import os

# Load environment variables from the .env file (if present)
load_dotenv()

# Access environment variables as if they came from the actual environment
SECRET_KEY = os.getenv('OPEN_AI_API_KEY')

st.title("Ask me anything")

input_text = st.text_input(label="Please enter you text here..")

llm = OpenAI(api_key = SECRET_KEY, temperature=0.6)

my_prompt = PromptTemplate(
    input_variables=["content"],
    template = "{content}"
)

chain = LLMChain(llm = llm, prompt = my_prompt)
response = chain.run(input_text)


st.markdown(response)