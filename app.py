import streamlit as st

from langchain.prompts import PromptTemplate
from langchain.llms import ctransformers


class GetBlogModel():
    def __init__(self):
        self.llm = ctransformers(model="models/llama-2-7b-chat.ggmlv3.q8_0.bin",
                                model_type='llama',
                                config={"max_new_tokens": 256,
                                        "temperature": 0.01})


    def getResponse(self, blog_topic, blog_style, blog_len):
        template = """
                    You are a blog writer. Please write me a blog on the 
                    topic {blog_topic} for {blog_style}, with a minimum 
                    word count of {blog_len}
                    """
        
        prompt = PromptTemplate(input_variables=["topic", "style", "length"],
                                template=template)
        
        return self.llm(prompt.format(topic=blog_topic, style=blog_style, length=blog_len))
    

def main():
    # Initializing llm model for blog generation
    blog_generator = GetBlogModel()

    # Configuring app landing page
    st.set_page_config(page_title="Blog Generator 9000",
                       page_icon="📓",
                       layout="centered",
                       initial_sidebar_state="collapsed")

    # Setting title of the page
    st.head("Blog Generator 9000 📓")

    # Getting topic, len of blog, and blog style from user
    blog_topic = st.text_input("Topic")
    col1, col2 = st.columns([5,5])
    with col1: blog_len = st.text_input("Desired Length of the Blog")
    with col2: blog_style = st.selectbox("Blog Style", ("Casual Reader", "Engineers", "Researchers"))

    # Getting respose from the LLM model
    if st.button("Generate Blog"):
       st.write(blog_generator.getResponse(blog_topic, blog_style, blog_len))


if __name__ == "__main__":
    main()
