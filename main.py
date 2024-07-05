import streamlit as st
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from dotenv import load_dotenv
import os

load_dotenv()

OPENAIKEY = st.secrets["API_KEY"]

st.title("Ask me anything")

input_text = st.text_input(label="Please enter you text here..")
tone = st.sidebar.selectbox("Select Tone", ("Friend", "Assistant", "Expert"))
word_limit = st.sidebar.slider("Select Word limit", min_value=10, max_value=50)


llm = OpenAI(api_key = OPENAIKEY, temperature=0.6)

my_prompt = PromptTemplate(
    input_variables=["content","tone","word_limit"],
    template = "Act as {tone}, tell me {content}. word limit is {word_limit}"
)

chain = LLMChain(llm = llm, prompt = my_prompt)
response = chain.run({"content":input_text, "tone":tone, "word_limit":word_limit})

if input_text == "":
    response = ""
else:
    st.markdown(response)