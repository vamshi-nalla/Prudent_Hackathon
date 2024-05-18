import streamlit as st
from src.helper import text_input, llm_model_object

def main():
    st.title("Building an LLM Text Generation Tool for Hackathon")

    # Text input field
    text = st.text_input(label="Ask me anything:", key="user_input")

    # Process text using LLM model
    
    if text:  # Process only if text is provided
        with st.spinner("Thinking..."):
            response = llm_model_object(text)
            st.text_area(label="Response:", value=response, height=350)
    else:
        st.info("Please enter your question.")

if __name__ == "__main__":
    main()
