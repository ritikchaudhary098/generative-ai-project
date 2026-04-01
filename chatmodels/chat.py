from dotenv import load_dotenv
import os
from langchain_mistralai import ChatMistralAI

# Load API key
load_dotenv()

# Load model
model = ChatMistralAI(model="mistral-small-2603")

print("🤖 Chatbot started! (type 'exit' to stop)\n")

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        print("👋 Goodbye!")
        break

    response = model.invoke(user_input)
    print("AI:", response.content)