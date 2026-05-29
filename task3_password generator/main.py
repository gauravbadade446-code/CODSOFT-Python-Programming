import tkinter as tk
from tkinter import messagebox
import random
import string
import pyperclip


class PasswordGenerator:

    def __init__(self):

        self.root = tk.Tk()
        self.root.title("Password Generator")
        self.root.geometry("500x400")

        tk.Label(self.root, text="Password Length").pack()

        self.length = tk.Entry(self.root)
        self.length.pack()

        self.password_text = tk.StringVar()

        tk.Button(
            self.root,
            text="Generate",
            command=self.generate_password
        ).pack(pady=10)

        tk.Entry(
            self.root,
            textvariable=self.password_text,
            width=40
        ).pack()

        tk.Button(
            self.root,
            text="Copy",
            command=self.copy_password
        ).pack(pady=10)

    def generate_password(self):

        try:
            length = int(self.length.get())

            characters = (
                string.ascii_letters +
                string.digits +
                string.punctuation
            )

            password = ''.join(
                random.choice(characters)
                for _ in range(length)
            )

            self.password_text.set(password)

        except ValueError:
            messagebox.showerror(
                "Error",
                "Enter valid number"
            )

    def copy_password(self):
        pyperclip.copy(self.password_text.get())
        messagebox.showinfo("Copied", "Password copied!")

    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    app = PasswordGenerator()
    app.run()