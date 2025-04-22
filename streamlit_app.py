import streamlit as st
from langchain_openai import AzureChatOpenAI

st.title("🦜🔗 Quickstart App")

openai_api_key = st.sidebar.text_input("OpenAI API Key", type="password")
azure_endpoint = st.sidebar.text_input("Azure OpenAI Endpoint", type="password")




def generate_response_azure(input_text):
    model = AzureChatOpenAI(
        azure_deployment="gpt-4o",
        openai_api_version="2024-08-01-preview",
        openai_api_key=openai_api_key,
        azure_endpoint=azure_endpoint,
        temperature=0.7,
    )
    response = model.invoke(input_text)
    st.markdown(response.content, unsafe_allow_html=True)


with st.form("my_form"):
    text = st.text_area(
        "Enter text:",
        "What are the three key pieces of advice for learning how to code?",
    )
    submitted = st.form_submit_button("Submit")
    if not openai_api_key:
        st.warning("Please enter your OpenAI API key!", icon="⚠")
    if not azure_endpoint:
        st.warning("Please enter your Azure OpenAI endpoint!", icon="⚠")
    if submitted and openai_api_key and azure_endpoint:
        generate_response_azure(text)
        st.success("Response generated successfully!")