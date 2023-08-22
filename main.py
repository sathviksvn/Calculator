import tkinter as tk
import math

def on_digit_click(digit):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + str(digit))

def on_operator_click(operator):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + operator)

def on_clear_click():
    entry.delete(0, tk.END)

def on_equals_click():
    try:
        expression = entry.get()
        result = eval(expression)
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

def on_sqrt_click():
    try:
        value = float(entry.get())
        result = math.sqrt(value)
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

def calculate_factorial(num):
    try:
        value = int(num)
        result = math.factorial(value)
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

def on_backspace_click():
    current = entry.get()
    entry.delete(len(current) - 1)

# Create the main application window
root = tk.Tk()
root.title("Calculator")
root.geometry("250x380")

# Create GUI elements
entry = tk.Entry(root, width=20, font=("Helvetica", 20))
entry.grid(row=0, column=0, columnspan=4)

buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3),
    ("√", 5, 0), ("!", 5, 1), ("<-", 5, 2), ("Clear", 5, 3),
]

for button_text, row, column in buttons:
    if button_text == "!":
        button = tk.Button(root, text=button_text, width=5, height=2,
                           font=("Helvetica", 14), command=lambda text=button_text: calculate_factorial(entry.get()))
    elif button_text == "√":
        button = tk.Button(root, text=button_text, width=5, height=2,
                           font=("Helvetica", 14), command=on_sqrt_click)
    elif button_text == "Clear":
        button = tk.Button(root, text=button_text, width=5, height=2,
                           font=("Helvetica", 14), command=on_clear_click)
    elif button_text == "<-":
        button = tk.Button(root, text=button_text, width=5, height=2,
                           font=("Helvetica", 14), command=on_backspace_click)
    elif button_text == "=":
        button = tk.Button(root, text=button_text, width=5, height=2,
                           font=("Helvetica", 14), command=on_equals_click)
    else:
        button = tk.Button(root, text=button_text, width=5, height=2,
                           font=("Helvetica", 14), command=lambda text=button_text: on_digit_click(text) if text.isnumeric() or text in [".", "="] else on_operator_click(text))

    button.grid(row=row, column=column)

# Start the main event loop
root.mainloop()
