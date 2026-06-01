from tkinter import *

screen = Tk()
screen.title("Inches to Cm")

lbl1 = Label(text="Inches to Cm")
lbl2 = Label(text="Enter Inches")
entry = Entry()
def math():
    sum = entry.get()
    sum = float(sum)
    sum *= 2.54
    textbox.insert(END, sum)

textbox = Text(height=1)
button = Button(text="convert", command=math)
lbl1.pack()
lbl2.pack()
entry.pack()
button.pack()
textbox.pack()
screen.mainloop()