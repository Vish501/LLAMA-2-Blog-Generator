import streamlit as st

from langchain.prompts import PromptTemplate
from langchain.llms import ctransformers
from transformers import AutoModel


class GetBlogModel:
    def __init__(self, model_id):
        self.llm = AutoModel.from_pretrained(model_id)
    

def main():
    # Initializing llm model for blog generation
    blog_ai = GetBlogModel("TheBloke/Llama-2-7B-Chat-GGML")

    # Configuring app landing page
    st.set_page_config(page_title="Blog Generator 9000",
                       page_icon="📓",
                       layout="centered",
                       initial_sidebar_state="collapsed")

    # Setting title of the page
    st.head("Blog Generator 9000 📓")

if __name__ == "__main__":
    main()
