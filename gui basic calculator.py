from tkinter import *
#defining the workings of the buttons
def button_pressed(num):
    global equation_text
    equation_text+= str(num)
    equation_label.set(equation_text)
def equals():
    global equation_text
    try:
        total = str(eval(equation_text))
        equation_label.set(total)
        equation_text = total
    except SyntaxError:
        equation_label.set("Syntax Error")
        equation_text = equation_text
    except ZeroDivisionError:
        equation_label.set("Arithmetic Error")
        equation_text = equation_text
def clear():
    global equation_text
    equation_text = ""
    equation_label.set(equation_text)
def sqaure():
    global equation_text
    power1 = str(int(equation_text)**2)
    equation_label.set(power1)
    equation_text = power1
def root():
    global equation_text
    rooted = str(int(equation_text)**0.5)
    equation_label.set(rooted)
def cube():
    global equation_text
    cubed = str(int(equation_text)**3)
    equation_label.set(cubed)
    equation_text = cubed
def last_one_clr():
    global equation_text
    equation_text = equation_text[:-1]
    equation_label.set(equation_text)
def only_pass():
    pass
#making the window:
window = Tk()
window.title("Calculator program")
window.geometry("500x500")
window.resizable(False, False)

#frame work
equation_text = ""
equation_label = StringVar()
label = Label(window, textvariable=equation_label, font=("Arial", 25), bg="white", width=30, height=3)
label.pack(pady=10)

frame = Frame(window)
frame.pack()

#buttons:

#button 1st row:
button1 = Button(frame, text=1, height=4, width=9, font=35, command=lambda :button_pressed(1))
button1.grid(row=0,column=0)
button2 = Button(frame, text=2, height=4, width=9, font=35, command=lambda :button_pressed(2))
button2.grid(row=0,column=1)
button3 = Button(frame, text=3, height=4, width=9, font=35, command=lambda :button_pressed(3))
button3.grid(row=0,column=2)

#button 2nd row:
button4 = Button(frame, text=4, height=4, width=9, font=35, command=lambda :button_pressed(4))
button4.grid(row=1,column=0)
button5 = Button(frame, text=5, height=4, width=9, font=35, command=lambda :button_pressed(5))
button5.grid(row=1,column=1)
button6 = Button(frame, text=6, height=4, width=9, font=35, command=lambda :button_pressed(6))
button6.grid(row=1,column=2)

#button 3rd row:
button7 = Button(frame, text=7, height=4, width=9, font=35, command=lambda :button_pressed(7))
button7.grid(row=2,column=0)
button8 = Button(frame, text=8, height=4, width=9, font=35, command=lambda :button_pressed(8))
button8.grid(row=2,column=1)
button9 = Button(frame, text=9, height=4, width=9, font=35, command=lambda :button_pressed(9))
button9.grid(row=2,column=2)

#button 4th row:
button0 = Button(frame, text=0, height=4, width=9, font=35, command=lambda :button_pressed(0))
button0.grid(row=3,column=0)

#operation signs:
plus = Button(frame, text="+", height=4, width=9, font=35, command=lambda :button_pressed("+"))
plus.grid(row=0,column=3)
minus = Button(frame, text="-", height=4, width=9, font=35, command=lambda :button_pressed("-"))
minus.grid(row=1,column=3)
divide = Button(frame, text="/", height=4, width=9, font=35, command=lambda :button_pressed("/"))
divide.grid(row=2,column=3)
multiply = Button(frame, text="*", height=4, width=9, font=35, command=lambda :button_pressed("*"))
multiply.grid(row=3,column=3)
equals_to = Button(frame, text="=", height=4, width=9, font=35, command=equals)
equals_to.grid(row=3,column=2)
decimal = Button(frame, text=".", height=4, width=9, font=35, command=lambda :button_pressed("."))
decimal.grid(row=3,column=1)
power = Button(frame, text="x²", height=4, width=9, font=35, command=sqaure)
power.grid(row=4,column=0)
rooted2 = Button(frame, text="√", height=4, width=9, font=35, command=root)
rooted2.grid(row=4,column=1)
cubed2 = Button(frame, text="x^3", height=4, width=9, font=35, command=cube)
cubed2.grid(row=4,column=2)

#clear button:
clear_to = Button(frame, text="CLEAR", height=4, width=9, font=35, command=clear)
clear_to.grid(row=4,column=3)

#centering the canvas
window.update()

window.width = window.winfo_width()
window.height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
x = int((screen_width/2) - (window.width/2))
y = int((screen_height/2) - (window.height/2))
window.geometry(f"{window.width}x{window.height}+{x}+{y-100}")

#responsive keys
window.bind('<Key>', lambda event: button_pressed(event.char))
window.bind("<Return>", lambda event: equals())
window.bind('<=>', lambda event: equals())
window.bind("<BackSpace>", lambda event: clear())
window.bind("<Tab>", lambda event: last_one_clr())
window.bind("<space>", lambda event: only_pass())
li = "qwertyuiopasdfghjklzxcvbnm"
for char in li:
    window.bind(char, lambda event: only_pass())


window.mainloop()