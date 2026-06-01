from tkinter import *
from tkinter import messagebox
root = Tk()
root.geometry("200x200")

def msg():
    messagebox.showwarning("Alert", "Stop! Virus found!")
button = Button(root, text="Warning", command=msg)
button.place(x=40, y=80)
button.pack()
def msg1():
    messagebox.showinfo("Info", "The above button isnt actually a virus :P")
button1 = Button(root, text="Info", command=msg1)
button1.place(x=40, y=90)
button1.pack()
def msg2():
    messagebox.showerror("Error", "Goodbye world")
button2 = Button(root, text="Error", command=msg2)
button2.place(x=40, y=100)
button2.pack()
def msg3():
    messagebox.askquestion("Alert", "Yes or no?")
button3 = Button(root, text="Question", command=msg3)
button3.place(x=40, y=110)
button3.pack()
def msg4():
    messagebox.askokcancel("Alert", "Proceed?")
button4 = Button(root, text="OK/Cancel", command=msg4)
button4.place(x=40, y=120)
button4.pack()
def msg5():
    messagebox.askyesno("Alert", "Would you like an imaginary cookie?")
button5 = Button(root, text="Yes/No", command=msg5)
button5.place(x=40, y=130)
button5.pack()
def msg6():
    messagebox.askretrycancel("Alert", "Retry procedure?")
button6 = Button(root, text="Retry/Cancel", command=msg6)
button6.place(x=40, y=140)
button6.pack()

root.mainloop()