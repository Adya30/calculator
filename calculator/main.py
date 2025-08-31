import tkinter

button_calc = [
    ["AC", "+/-", "%", "/"],
    ["7", "8", "9", "x"],
    ["4", "5", "6", "-"],
    ["1", "2", "3", "+"],
    ["0", ".", " ", "="]
]

right_symbols= ["/", "x", "-", "+", "="]
top_symbols = ["AC", "+/-", "%"]

row_count = len(button_calc)
column_count = len(button_calc[0])

orange = "#FFA915"
black = "#1C1C1C"
blue = "#4D1EAC"
green= "#AECE0C"
white = "#FFFFFF"

# main window
window = tkinter.Tk()
window.iconbitmap("logo.ico")
window.title("Calculator")
window.resizable(False, False)

frame = tkinter.Frame(window)
label = tkinter.Label(frame, text="0", font=("Arial", 45), background=black, foreground=white, anchor="e", width=column_count) 

label.grid(row=0, column=0, columnspan=column_count, sticky="we")

for row in range(row_count):
    for column in range(column_count):
        value = button_calc[row][column]
        button = tkinter.Button(frame, text=value, font=("Arial", 30), width=column_count-1, height=1, command=lambda value=value: button_click(value))

        if value in top_symbols:
            button.config(foreground=black, background=orange)
        elif value in right_symbols:
            button.config(foreground=white, background=green)
        else:
            button.config(foreground=white, background=blue)
            
        button.grid(row=row+1, column=column)

frame.pack()

# + - *
A = "0"
operator = None
B = None

def clear_all():
    global A, B, operator, reset_next
    A = None
    B = None
    operator = None
    reset_next = False  

def remove_0_decimal(num):
    if num % 1 == 0:
        num = int(num)
    return str(num)

def button_click(value):
    global right_symbols, top_symbols, label, A, B, operator, reset_next

    if value in right_symbols:
        if value == "=":
            if A is not None and operator is not None:
                B = label["text"]
                numA = float(A)
                numB = float(B)

                if operator == "+":
                    label["text"] = remove_0_decimal(numA + numB)
                elif operator == "-":
                    label["text"] = remove_0_decimal(numA - numB)
                elif operator == "x":
                    label["text"] = remove_0_decimal(numA * numB)
                elif operator == "/":
                    if numB == 0:
                        label["text"] = "Error"
                    else:
                        label["text"] = remove_0_decimal(numA / numB)

                clear_all()

        elif value in "+-x/":
            if operator is None:
                A = label["text"]
            operator = value
            reset_next = True  

    elif value in top_symbols:
        if value == "AC":
            clear_all()
            label["text"] = "0"

        elif value == "+/-":
            result = float(label["text"]) * -1
            label["text"] = remove_0_decimal(result)

        elif value == "%":
            result = float(label["text"]) / 100
            label["text"] = remove_0_decimal(result)

    else:
        if value == ".":
            if "." not in label["text"]:
                label["text"] += value
        elif value in "0123456789":
            if label["text"] == "0" or reset_next:
                label["text"] = value
                reset_next = False
            else:
                label["text"] += value

window.update()
window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

window_x = int((screen_width/2) - (window_width/2))
window_y = int((screen_height/2) - (window_height/2))

# format
window.geometry(f"{window_width}x{window_height}+{window_x}+{window_y}")

window.mainloop()