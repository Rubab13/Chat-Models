# Basic Conversation

from dotenv import load_dotenv
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage
from langchain_google_genai import GoogleGenerativeAI
import os

load_dotenv(override=True)
api_key = os.getenv("API_KEY")

model = GoogleGenerativeAI(model="gemini-pro", google_api_key=api_key)

messages = [
  SystemMessage(content="You are a lawyer."),
  HumanMessage(content="What is the meaning of the term 'ultravirus'?")
]

response = model.invoke(messages)
print(response)

# Question: If we do not give context to the model through system message, is there a change in response? like will the model not respond or will not respond accurately, if we do not provide context?
# Question: How is context maintained through the conversation?