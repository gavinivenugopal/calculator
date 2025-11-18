import tkinter as tk

# Function to update the expression in the entry field
def button_click(value):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + str(value))

# Function to evaluate the expression
def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# Function to clear the entry field
def clear():
    entry.delete(0, tk.END)

# Create the main window
root = tk.Tk()
root.title("Calculator")
root.geometry("400x600")

# Entry widget to display the expression/result
entry = tk.Entry(root, width=16, font=("Arial", 24), borderwidth=2, relief="solid", justify="right")
entry.grid(row=0, column=0, columnspan=4)

# Buttons for numbers and operations
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
]

# Create and place buttons on the window
for (text, row, col) in buttons:
    if text == '=':
        button = tk.Button(root, text=text, width=10, height=3, font=("Arial", 18), command=calculate)
    else:
        button = tk.Button(root, text=text, width=10, height=3, font=("Arial", 18), command=lambda value=text: button_click(value))
    button.grid(row=row, column=col)

# Clear button
clear_button = tk.Button(root, text="C", width=10, height=3, font=("Arial", 18), command=clear)
clear_button.grid(row=5, column=0, columnspan=2)

# Run the application
root.mainloop()
