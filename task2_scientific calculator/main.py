import tkinter as tk
import math

class Calculator:

    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Scientific Calculator")
        self.root.geometry("400x600")
        self.root.configure(bg="#1e1e1e")
        self.root.resizable(False, False)

        self.expression = ""
        self.input_text = tk.StringVar()

        input_frame = tk.Frame(self.root, bg="#1e1e1e")
        input_frame.pack(pady=10)

        input_field = tk.Entry(
            input_frame,
            textvariable=self.input_text,
            font=("Arial", 24),
            width=20,
            bd=5,
            relief=tk.FLAT,
            justify='right',
            bg="#2d2d2d",
            fg="white",
            insertbackground="white"
        )

        input_field.pack(ipady=20, padx=10)

        buttons = [
            ['7', '8', '9', '/'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '-'],
            ['0', '.', '=', '+'],
            ['sin', 'cos', 'tan', 'C']
        ]

        for row in buttons:
            frame = tk.Frame(self.root, bg="#1e1e1e")
            frame.pack(expand=True, fill='both', padx=5, pady=5)

            for btn in row:
                button = tk.Button(
                    frame,
                    text=btn,
                    font=("Arial", 18),
                    bg="#333333",
                    fg="white",
                    activebackground="#555555",
                    activeforeground="white",
                    bd=0,
                    relief=tk.FLAT,
                    command=lambda b=btn: self.click(b)
                )

                button.pack(side='left', expand=True, fill='both', padx=3, pady=3)

    def click(self, item):

        try:
            if item == "=":
                result = str(eval(self.expression))
                self.input_text.set(result)
                self.expression = result

            elif item == "C":
                self.expression = ""
                self.input_text.set("")

            elif item == "sin":
                value = math.sin(math.radians(float(self.expression)))
                self.expression = str(value)
                self.input_text.set(self.expression)

            elif item == "cos":
                value = math.cos(math.radians(float(self.expression)))
                self.expression = str(value)
                self.input_text.set(self.expression)

            elif item == "tan":
                value = math.tan(math.radians(float(self.expression)))
                self.expression = str(value)
                self.input_text.set(self.expression)

            else:
                self.expression += str(item)
                self.input_text.set(self.expression)

        except Exception:
            self.input_text.set("Error")
            self.expression = ""

        self.root.update_idletasks()

    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    calc = Calculator()
    calc.run()