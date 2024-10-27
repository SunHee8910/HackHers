import tkinter as tk


responses = {
    "how do i invest in stocks?": "Investing in stocks involves buying shares in a company with the expectation that they’ll increase in value over time, allowing you to profit from that growth.",
    "help": "I'm here to answer basic questions. Type 'bye' to exit.",
    "bye": "Goodbye! Have a great day!",
}


def get_response(user_input):
    return responses.get(user_input.lower(), "I don't understand that.")

def send_message():
    user_input = user_entry.get()
    chat_window.insert(tk.END, "You: " + user_input + "\n")
    response = get_response(user_input)
    chat_window.insert(tk.END, "Bot: " + response + "\n\n")
    user_entry.delete(0, tk.END)


root = tk.Tk()
root.title("Chatbot")


chat_window = tk.Text(root, bd=1, bg="light gray", width=50, height=8)
chat_window.pack()


user_entry = tk.Entry(root, width=30)
user_entry.pack()


send_button = tk.Button(root, text="Send", command=send_message)
send_button.pack()

root.mainloop()