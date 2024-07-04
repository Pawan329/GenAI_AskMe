import streamlit as st
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

st.title("Ask me anything")

OPENAIKEY = st.text_input(label="Enter your API Key he..")

if OPENAIKEY:
    input_text = st.text_input(label="Please enter you text here..")

llm = OpenAI(api_key = OPENAIKEY, temperature=0.6)

my_prompt = PromptTemplate(
    input_variables=["content"],
    template = "{content}"
)

chain = LLMChain(llm = llm, prompt = my_prompt)
response = chain.run(input_text)


st.markdown(response)