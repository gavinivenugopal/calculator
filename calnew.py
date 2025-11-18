import tkinter as tk

root = tk.Tk()
root.title("Calculator v2.0")
root.geometry("400x550")
root.config(bg="#1e1e1e")

# ---------------------------
#  Functions
# ---------------------------

expression = ""

def update_display(value):
    global expression
    expression += str(value)
    display_var.set(expression)

def clear():
    global expression
    expression = ""
    display_var.set(expression)

def backspace():
    global expression
    expression = expression[:-1]
    display_var.set(expression)

def calculate():
    global expression
    try:
        # Replace % with /100 for calculation
        expr = expression.replace("%", "/100")

        result = str(eval(expr))
        display_var.set(result)
        expression = result
    except:
        display_var.set("Error")
        expression = ""

# ---------------------------
#  Display
# ---------------------------

display_var = tk.StringVar()

display = tk.Entry(
    root, textvariable=display_var,
    font=("Arial", 28),
    bd=0, relief="solid",
    fg="white", bg="#2d2d2d",
    justify="right"
)
display.pack(fill="both", ipadx=10, ipady=20, padx=15, pady=20)

# ---------------------------
#  Button Definitions
# ---------------------------

buttons = [
    ("C", clear), ("⌫", backspace), ("%", lambda: update_display('%')), ("/", lambda: update_display('/')),
    ("7", lambda: update_display('7')), ("8", lambda: update_display('8')), ("9", lambda: update_display('9')), ("*", lambda: update_display('*')),
    ("4", lambda: update_display('4')), ("5", lambda: update_display('5')), ("6", lambda: update_display('6')), ("-", lambda: update_display('-')),
    ("1", lambda: update_display('1')), ("2", lambda: update_display('2')), ("3", lambda: update_display('3')), ("+", lambda: update_display('+')),
    ("00", lambda: update_display('00')), ("0", lambda: update_display('0')), (".", lambda: update_display('.')), ("=", calculate)
]

# ---------------------------
#  Create Buttons (Grid)
# ---------------------------

btn_frame = tk.Frame(root, bg="#1e1e1e")
btn_frame.pack()

row = 0
col = 0

for text, command in buttons:
    btn = tk.Button(
        btn_frame,
        text=text,
        command=command,
        font=("Arial", 20),
        width=5, height=2,
        fg="white",
        bg="#3a3a3a",
        activebackground="#555",
        activeforeground="white",
        bd=0,
        highlightthickness=0
    )
    btn.grid(row=row, column=col, padx=5, pady=5)

    col += 1
    if col > 3:
        col = 0
        row += 1

# ---------------------------
#  Keyboard Support
# ---------------------------

def key_event(event):
    key = event.char

    if key.isdigit() or key in "+-*/.%":
        update_display(key)
    elif key == "\r":  # Enter
        calculate()
    elif key == "\x08":  # Backspace
        backspace()

root.bind("<Key>", key_event)

root.mainloop()
