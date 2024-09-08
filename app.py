import streamlit as st
from langchain_groq import ChatGroq
from groq import Groq
from langchain_core.prompts import ChatPromptTemplate

llm = ChatGroq(groq_api_key = "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",
               model="llama3-70b-8192",
               temperature=0.5)




# 1. Header
st.title('Ask me Anything')

# 2. User Input
user_input = st.text_input('Enter some text:')

response = llm.invoke(user_input)
output = response.content

# 3. Show Output
if user_input:
    st.write(f'User: {user_input}')
    st.write(f'System: {output}')
else:
    st.write('Please enter some text above.')






