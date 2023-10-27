import openai
import os
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

print("Welcome to the GPT-3 Chatbot!")
print("Enter exit to quit the program.")
messages = []

while True:
    user_message = input("USER: ")

    if user_message.lower() == "exit":
        break

    messages.append({"role": "user", "content": user_message})
    response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)
    chat_message = response["choices"][0]["message"]["content"]
    print(f"BOT: {chat_message}")

    messages.append({"role": "assistant", "content": chat_message})
