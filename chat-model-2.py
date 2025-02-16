# with langchain
from langchain_google_genai import GoogleGenerativeAI
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("API_KEY")

model = GoogleGenerativeAI(model="gemini-pro", google_api_key=api_key)
response = model.invoke("Hello")
print(response)