import google.generativeai as genai
from dotenv import load_dotenv
import os

print("Hey prudent!")
load_dotenv()

GOOGLE_API_KEY=os.getenv("GOOGLE_API_KEY")
os.environ["GOOGLE_API_KEY"]=GOOGLE_API_KEY

def text_input():
    user_text = input("Enter your text: ")
    return user_text

def llm_model_object(user_text):
    genai.configure(api_key=google_api_key)
    model = genai.GenerativeModel('gemini-pro')
    response=model.generate_content(user_text)
    result=response.text
    return result

