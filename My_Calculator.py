from tkinter import *
import customtkinter as ctk
import multiprocessing as mp
import sympy as sp

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

root = ctk.CTk()

bg_color = "#121212"
button_color = "#1e1e1e"
button_hover_color = "#262626"
accent_color = "#4fd1c5"
accent_hover_color = "#37cfe7"

root.title("Basic Calculator")
root.geometry("400x600")
root.iconbitmap("calculator.ico")
root.resizable(False, False)
root.configure(fg_color = bg_color)



display_frame = ctk.CTkFrame(root, fg_color=bg_color)
display_frame.pack(fill="x", padx = 20, pady = (40,10))

result = ctk.CTkEntry(display_frame, font = ("Arial", 64), justify = "right", fg_color=bg_color, border_width=0)
result.pack(fill = "x", expand = True, padx = 20, pady = (0, 40))
result.insert(0, "0")
result.configure(state = 'readonly')

global current_expression 
global flag
global operators
current_expression = "0"
flag = 0
operators = ['÷', '×', '-', '+', '^']

def key_press(event):
    key = event.char
    keysym = event.keysym
    if key == '=' or keysym == "Return":
        calculate()
    elif key.lower() == 'c':
        clear()
    elif keysym == "BackSpace":
        backspace()
    elif key == '*':
        add_to_expression('×')
    elif key == '/':
        add_to_expression('÷')
    elif key in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '+', '-', '*', '/', '.', '^', '(', ')','e']:
        add_to_expression(key)

root.bind('<Key>', key_press)

def button_click(key):
    if key == "=":
        calculate()
    elif key == "⬅️":
        backspace()
    elif key == "C":
        clear()
    else:
        add_to_expression(key)

def calculate():
    global current_expression
    global flag 
    global operators
    try:
        if "\u03C0" in current_expression:
            prev = -1
            next = -1
            prev = current_expression.index('\u03C0') - 1
            next = current_expression.index('\u03C0') + 1
            prev = prev if prev in range(len(current_expression)) else -1
            next = next if next in range(len(current_expression)) else -1
  
            if prev != -1:
                if current_expression[prev] in operators or current_expression[prev] == '(':
                    current_expression = current_expression.replace("\u03C0", "3.14159", 1)
                    calculate()
            elif next != -1:
                if current_expression[next] in operators or current_expression[next] == ')':
                    current_expression = current_expression.replace("\u03C0", "3.14159", 1)
                    calculate()
            else :
                current_expression = "3.14159"

        if "e" in current_expression:
            prev = -1
            next = -1
            prev = current_expression.index('e') - 1
            next = current_expression.index('e') + 1
            prev = prev if prev in range(len(current_expression)) else -1
            next = next if next in range(len(current_expression)) else -1

            if prev != -1:
                if current_expression[prev] in operators or current_expression[prev] == '(':
                    current_expression = current_expression.replace("e", "2.71828", 1)
                    calculate()
            elif next != -1:
                if current_expression[next] in operators or current_expression[next] == ')':
                    current_expression = current_expression.replace("e", "2.71828", 1)
                    calculate()
            else:
                current_expression = "2.71828"
        if  '^' in current_expression:
            current_expression = current_expression.replace('^', '**')
        if  '÷' in current_expression:
            current_expression = current_expression.replace('÷', '/')
        if  '×' in current_expression:
            current_expression = current_expression.replace('×', '*')
        #
       
        answer = eval(current_expression)
        if (answer - int(answer)) != 0:
            pass
        else:
            answer = int(answer)
        current_expression = str(answer)
        flag = 1
    except:
        current_expression = "Error"
        flag = 1
    update_result()



def clear():
    global current_expression 
    current_expression = "0"
    update_result()

def backspace():
    global current_expression
    global flag
    if(flag):
        current_expression = "0"
        flag = 0
    else:
        current_expression = current_expression[:-1]
    if current_expression == "":
        current_expression = "0"
    update_result()

def add_to_expression(key):
    global current_expression
    global flag
    global operators 
    if(flag):
        if key in operators:
            current_expression += key
            flag = 0
        else:
            result.delete(0, ctk.END)
            current_expression = key
            flag = 0
    else:
        if current_expression == "0" or current_expression == "" or current_expression == "Error":
            current_expression = key
        else:
            if current_expression[-1] in operators:
                if key in operators:
                    current_expression = current_expression[:-1]
            current_expression += key
    update_result()

def update_result():
    global current_expression
    result.configure(state = 'normal')
    result.delete(0, ctk.END)
    result.insert(0, current_expression)

    text_length = len(current_expression)
    if text_length > 7:
        new_font_size = 40
    else:
        new_font_size = 64

    result.configure(font = ("Arial", new_font_size), state = "readonly")


button_frame = ctk.CTkFrame(root, fg_color=bg_color)
button_frame.pack(fill="both", expand = True, padx = 20, pady = (0,20))

button_1 = ctk.CTkButton(button_frame, text = "1", height = 60, width = 60, font = ("Arial", 24), command=lambda x="1":button_click(x), fg_color=button_color, hover_color=button_hover_color)
button_2 = ctk.CTkButton(button_frame, text = "2", height = 60, width = 60, font = ("Arial", 24), command=lambda x="2":button_click(x), fg_color=button_color, hover_color=button_hover_color)
button_3 = ctk.CTkButton(button_frame, text = "3", height = 60, width = 60, font = ("Arial", 24), command=lambda x="3":button_click(x), fg_color=button_color, hover_color=button_hover_color)
button_4 = ctk.CTkButton(button_frame, text = "4", height = 60, width = 60, font = ("Arial", 24), command=lambda x="4":button_click(x), fg_color=button_color, hover_color=button_hover_color)
button_5 = ctk.CTkButton(button_frame, text = "5", height = 60, width = 60, font = ("Arial", 24), command=lambda x="5":button_click(x), fg_color=button_color, hover_color=button_hover_color)
button_6 = ctk.CTkButton(button_frame, text = "6", height = 60, width = 60, font = ("Arial", 24), command=lambda x="6":button_click(x), fg_color=button_color, hover_color=button_hover_color)
button_7 = ctk.CTkButton(button_frame, text = "7", height = 60, width = 60, font = ("Arial", 24), command=lambda x="7":button_click(x), fg_color=button_color, hover_color=button_hover_color)
button_8 = ctk.CTkButton(button_frame, text = "8", height = 60, width = 60, font = ("Arial", 24), command=lambda x="8":button_click(x), fg_color=button_color, hover_color=button_hover_color)
button_9 = ctk.CTkButton(button_frame, text = "9", height = 60, width = 60, font = ("Arial", 24), command=lambda x="9":button_click(x), fg_color=button_color, hover_color=button_hover_color)
button_0 = ctk.CTkButton(button_frame, text = "0", height = 60, width = 140, font = ("Arial", 24), command=lambda x="0":button_click(x), fg_color=button_color, hover_color=button_hover_color)
point = ctk.CTkButton(button_frame, text = ".", height = 60, width = 60, font = ("Arial", 24), command=lambda x=".":button_click(x), fg_color=button_color, hover_color=button_hover_color)
equalto = ctk.CTkButton(button_frame, text = "=", height = 60, width = 60, font = ("Arial", 24), command=lambda x="=":button_click(x), fg_color=accent_color, hover_color=accent_hover_color, text_color="black")


button_power = ctk.CTkButton(button_frame, text = "^", height = 60, width = 60, font = ("Arial", 24), command=lambda x="^":button_click(x), fg_color=accent_color, hover_color=accent_hover_color, text_color="black")
left_parenthesis = ctk.CTkButton(button_frame, text = "(", height = 60, width = 60, font = ("Arial", 24), command=lambda x="(":button_click(x), fg_color=accent_color, hover_color=accent_hover_color, text_color="black")
right_parenthesis = ctk.CTkButton(button_frame, text = ")", height = 60, width = 60, font = ("Arial", 24), command=lambda x=")":button_click(x), fg_color=accent_color, hover_color=accent_hover_color, text_color="black")

divide = ctk.CTkButton(button_frame, text = "÷", height = 60, width = 60, font = ("Arial", 24), command=lambda x="÷":button_click(x), fg_color=accent_color, hover_color=accent_hover_color, text_color="black")
multiply = ctk.CTkButton(button_frame, text = "×", height = 60, width = 60, font = ("Arial", 24), command=lambda x="×":button_click(x), fg_color=accent_color, hover_color=accent_hover_color, text_color="black")
substract = ctk.CTkButton(button_frame, text = "-", height = 60, width = 60, font = ("Arial", 24), command=lambda x="-":button_click(x), fg_color=accent_color, hover_color=accent_hover_color, text_color="black")
add = ctk.CTkButton(button_frame, text = "+", height = 60, width = 60, font = ("Arial", 24), command=lambda x="+":button_click(x), fg_color=accent_color, hover_color=accent_hover_color, text_color="black")

button_pi = ctk.CTkButton(button_frame, text = "\u03C0", height = 60, width = 60, font = ("Arial", 24), command=lambda x="\u03C0":button_click(x), fg_color=accent_color, hover_color=accent_hover_color, text_color="black")
button_e = ctk.CTkButton(button_frame, text = "e", height = 60, width = 60, font = ("Arial", 24), command=lambda x="e":button_click(x), fg_color=accent_color, hover_color=accent_hover_color, text_color="black")
button_clear = ctk.CTkButton(button_frame, text = "C", height = 60, width = 60, font = ("Arial", 24), command=lambda x="C":button_click(x), fg_color=accent_color, hover_color=accent_hover_color, text_color="black")
button_backspace = ctk.CTkButton(button_frame, text = "←", height = 60, width = 60, font = ("Arial", 24), command=lambda x="⬅️":button_click(x), fg_color=accent_color, hover_color=accent_hover_color, text_color="black")



button_pi.grid(row = 0, column = 0, padx = 5, pady = 5, sticky = "nsew")
button_e.grid(row = 0, column = 1, padx = 5, pady = 5, sticky = "nsew")
button_clear.grid(row = 0, column = 2, padx = 5, pady = 5, sticky = "nsew")
button_backspace.grid(row = 0, column = 3, padx = 5, pady = 5, sticky = "nsew")

left_parenthesis.grid(row = 1, column = 0, padx = 5, pady = 5, sticky = "nsew")
right_parenthesis.grid(row = 1, column = 1, padx = 5, pady = 5, sticky = "nsew")
button_power.grid(row = 1, column = 2, padx = 5, pady = 5, sticky = "nsew")
divide.grid(row = 1, column = 3, padx = 5, pady = 5, sticky = "nsew")

button_7.grid(row = 2, column = 0, padx = 5, pady = 5, sticky = "nsew")
button_8.grid(row = 2, column = 1, padx = 5, pady = 5, sticky = "nsew")
button_9.grid(row = 2, column = 2, padx = 5, pady = 5, sticky = "nsew")
multiply.grid(row = 2, column = 3, padx = 5, pady = 5, sticky = "nsew")

button_4.grid(row = 3, column = 0, padx = 5, pady = 5, sticky = "nsew")
button_5.grid(row = 3, column = 1, padx = 5, pady = 5, sticky = "nsew")
button_6.grid(row = 3, column = 2, padx = 5, pady = 5, sticky = "nsew")
substract.grid(row = 3, column = 3, padx = 5, pady = 5, sticky = "nsew")

button_1.grid(row = 4, column = 0, padx = 5, pady = 5, sticky = "nsew")
button_2.grid(row = 4, column = 1, padx = 5, pady = 5, sticky = "nsew")
button_3.grid(row = 4, column = 2, padx = 5, pady = 5, sticky = "nsew")
add.grid(row = 4, column = 3, padx = 5, pady = 5, sticky = "nsew")

button_0.grid(row = 5, column = 0, columnspan = 2, padx = 5, pady = 5, sticky = "nsew")
point.grid(row = 5, column = 2, padx = 5, pady = 5, sticky = "nsew")
equalto.grid(row = 5, column = 3, padx = 5, pady = 5, sticky = "nsew")

for i in range(6):
    button_frame.grid_rowconfigure(i, weight = 1)
for i in range(4):
    button_frame.grid_columnconfigure(i, weight = 1)



root.mainloop()

