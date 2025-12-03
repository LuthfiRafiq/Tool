import requests
import os

API_KEY = "MASUKKAN_API_KEY_MU"
API_URL = "https://api.deepseek.com/v1/chat/completions"

def banner():
    os.system("clear" if os.name != "nt" else "cls")
    print(r"""
██████╗ ███████╗███████╗███████╗███████╗██╗  ██╗███████╗██╗  ██╗
██╔══██╗██╔════╝██╔════╝██╔════╝██╔════╝██║ ██╔╝██╔════╝██║  ██║
██████╔╝█████╗  ███████╗███████╗█████╗  █████╔╝ ███████╗███████║
██╔══██╗██╔══╝  ╚════██║╚════██║██╔══╝  ██╔═██╗ ╚════██║██╔══██║
██║  ██║███████╗███████║███████║███████╗██║  ██╗███████║██║  ██║
╚═╝  ╚═╝╚══════╝╚══════╝╚══════╝╚══════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
                 Chatbot DeepSeek API
-------------------------------------------------------------
    """)

def ask_deepseek(prompt):
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {API_KEY}"
    }

    data = {
        "model": "deepseek-chat",
        "messages": [
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.8
    }

    response = requests.post(API_URL, json=data, headers=headers)
    return response.json()["choices"][0]["message"]["content"]

banner()
print("Ketik 'exit' untuk keluar\n")

while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit"]:
        print("\nKeluar dari Deepseek AI...")
        break

    try:
        reply = ask_deepseek(user_input)
        print("AI :", reply)
    except Exception as e:
        print("Error:", e)