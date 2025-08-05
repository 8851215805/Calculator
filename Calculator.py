import tkinter as tk
from tkinter import messagebox


class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Perfect Calculator")
        self.root.geometry("400x500")
        self.root.resizable(False, False)

        self.expression = ""

        # Input display
        self.input_text = tk.StringVar()
        input_frame = tk.Frame(self.root)
        input_frame.pack(side=tk.TOP, fill=tk.BOTH)

        input_field = tk.Entry(input_frame, textvariable=self.input_text, font=('Arial', 24), bd=10,
                               insertwidth=2, relief='ridge', justify='right')
        input_field.pack(fill=tk.BOTH, ipadx=8, ipady=15, padx=10, pady=10)

        # Buttons
        btns_frame = tk.Frame(self.root)
        btns_frame.pack()

        buttons = [
            ['7', '8', '9', '/'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '-'],
            ['0', '.', 'C', '+'],
            ['(', ')', '=', '']
        ]

        for r, row in enumerate(buttons):
            for c, char in enumerate(row):
                if char == '':
                    continue
                if char == 'C':
                    btn = tk.Button(btns_frame, text=char, fg='white', bg='red',
                                    font=('Arial', 18), width=5, height=2, command=self.clear)
                elif char == '=':
                    btn = tk.Button(btns_frame, text=char, fg='white', bg='green',
                                    font=('Arial', 18), width=5, height=2, command=self.calculate)
                else:
                    btn = tk.Button(btns_frame, text=char,
                                    font=('Arial', 18), width=5, height=2,
                                    command=lambda ch=char: self.press(ch))
                btn.grid(row=r, column=c, padx=5, pady=5)

    def press(self, value):
        self.expression += str(value)
        self.input_text.set(self.expression)

    def clear(self):
        self.expression = ""
        self.input_text.set("")

    def calculate(self):
        try:
            result = eval(self.expression)
            self.input_text.set(result)
            self.expression = str(result)
        except ZeroDivisionError:
            messagebox.showerror("Math Error", "Cannot divide by zero.")
            self.clear()
        except Exception:
            messagebox.showerror("Error", "Invalid Expression.")
            self.clear()


if __name__ == "__main__":
    root = tk.Tk()
    Calculator(root)
    root.mainloop()
