import tkinter as tk
from tkinter import messagebox
import random
import string

class PasswordGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Random Password Generator")

        self.canvas = tk.Canvas(root, width=400, height=350, bg="pink")
        self.canvas.pack()

        self.title_label = tk.Label(root, text="Random Password Generator", font=("Arial", 18), bg="pink")
        self.title_label.place(relx=0.5, rely=0.1, anchor="center")

        self.info_label = tk.Label(root, text="Enter password length:", font=("Arial", 12), bg="pink")
        self.info_label.place(relx=0.5, rely=0.3, anchor="center")

        self.length_entry = tk.Entry(root, font=("Arial", 12), width=10)
        self.length_entry.place(relx=0.5, rely=0.4, anchor="center")

        self.text_label = tk.Label(root, text="Enter additional text (optional):", font=("Arial", 12), bg="pink")
        self.text_label.place(relx=0.5, rely=0.5, anchor="center")

        self.text_entry = tk.Entry(root, font=("Arial", 12), width=20)
        self.text_entry.place(relx=0.5, rely=0.6, anchor="center")

        self.generate_button = tk.Button(root, text="Generate Password", font=("Arial", 12), command=self.generate_password)
        self.generate_button.place(relx=0.5, rely=0.7, anchor="center")

        self.output_label = tk.Label(root, text="", font=("Arial", 14), bg="pink")
        self.output_label.place(relx=0.5, rely=0.8, anchor="center")

    def generate_password(self):
        password_length_str = self.length_entry.get()

        if not password_length_str.isdigit():
            messagebox.showerror("Error", "Please enter a valid number for password length.")
            return

        password_length = int(password_length_str)

        if password_length < 4:
            messagebox.showerror("Error", "Password length should be at least 4 characters.")
            return

        additional_text = self.text_entry.get()

        if additional_text:
            if additional_text[0].islower():
                additional_text = additional_text[0].upper() + additional_text[1:]
            password_length -= len(additional_text)

        letters = string.ascii_letters
        digits = string.digits
        symbols = string.punctuation

        password_characters = [random.choice(letters.upper()), 
                               random.choice(letters.lower()), 
                               random.choice(digits), 
                               random.choice(symbols)]

        remaining_length = password_length - 4

        for _ in range(remaining_length):
            password_characters.append(random.choice(letters + digits + symbols))

        random.shuffle(password_characters)
        password = ''.join(password_characters)

        password = additional_text + password[:password_length]

        self.output_label.config(text=f"Generated Password: {password}")

def main():
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
