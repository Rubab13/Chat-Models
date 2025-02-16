import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv(override=True)
api_key = os.getenv("API_KEY")
genai.configure(api_key=api_key)

model = genai.GenerativeModel("gemini-pro")

response = model.generate_content("what is 81 divided by 9?")
print(response.text)