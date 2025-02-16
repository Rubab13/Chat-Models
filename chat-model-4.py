# Real Time Conversation

from dotenv import load_dotenv
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage
from langchain_google_genai import GoogleGenerativeAI
import os

load_dotenv(override=True)
api_key = os.getenv("API_KEY")

model = GoogleGenerativeAI(model="gemini-pro", google_api_key=api_key)

chat_history = []

chat_history.append(SystemMessage(content="You are a lawyer."))

while True:
  query = input("You: ")
  if query.lower() == "exit":
    break
  chat_history.append(HumanMessage(content=query))
  response = model.invoke(chat_history)
  chat_history.append(AIMessage(content=response))
  print("AI: ", response)
  
print("Chat History:\n", chat_history)