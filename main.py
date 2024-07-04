import streamlit as st
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

OPEN_AI_API_KEY = "sk-proj-oylfNhdmm0Tfk3Rm8jBGT3BlbkFJPEqXFMEv5MOrVNzW98B0"
st.title("Ask me anything")

input_text = st.text_input(label="Please enter you text here..")

llm = OpenAI(api_key=OPEN_AI_API_KEY, temperature=0.6)

my_prompt = PromptTemplate(
    input_variables=["content"],
    template = "{content}"
)

chain = LLMChain(llm = llm, prompt = my_prompt)
response = chain.run(input_text)


st.markdown(response)