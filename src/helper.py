import google.lgenerativeai as genai
from dotenv import load_dotenv
import os

print("Hello prudent recruiter..!, It was nice to meet you")
load_dotenv()

GOOGLE_API_KEY=os.getenv("GOOGLE_API_KEY")
os.environ["GOOGLE_API_KEY"]=GOOGLE_API_KEY

def text_input():
    user_text = input("Enter your text: ")
    return user_text

def llm_model_object(user_text):
    genai.configure(api_key=GOOGLE_API_KEY)
    model = genai.GenerativeModel('gemini-pro')
    response=model.generate_content(user_text)
    result=response.text
    return result

