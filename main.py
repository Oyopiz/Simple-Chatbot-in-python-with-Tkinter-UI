import tkinter as tk
import nltk


def send_message():
    # Get the user's message
    message = entry.get()

    # Tokenize the message
    tokens = nltk.word_tokenize(message)

    # Generate a response
    response = "I am a chatbot. I don't know how to respond to your message"

    # Check for specific words or phrases in the message
    if 'hello' in tokens:
        response = 'Hello! How are you today?'
    elif 'how are you' in tokens:
        response = "I am just a chatbot. I don't have feelings."


    # Display the conversation in the text area
    conversation.insert(tk.END, 'You: ' + message + '\n')
    conversation.insert(tk.END, 'Bot: ' + response + '\n')

    # Clear the text field
    entry.delete(0, tk.END)


# Create the UI
root = tk.Tk()
root.title('Chatbot')

# Add a text area to display the conversation
conversation = tk.Text(root, height=10, width=50)
conversation.pack()

# Add a label and text field for the message
label = tk.Label(root, text='Enter your message:')
label.pack()
entry = tk.Entry(root)
entry.pack()

# Add a button to send the message
button = tk.Button(root, text='Send', command=send_message)
button.pack()

# Run the program
root.mainloop()
