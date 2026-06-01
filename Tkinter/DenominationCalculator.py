from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

root = Tk()

root.title("Denomination Counter")
root.config(bg="lightblue")
root.geometry("650x400")

upload = Image.open("background.png")
upload = upload.resize((300, 300))
image = ImageTk.PhotoImage(upload)

label1 = Label(root, text="Hello!")

def msg():
    if messagebox.askokcancel("Alert", "Would you like to calculate denominations?"):
        topwin()

button1 = Button(root, text="Let's get started!", command=msg, bg="blue")
button1.pack()

def topwin():
    top = Toplevel()
    top.config(bg="green")
    top.geometry("400x400")

    toplabel = Label(top, text="Enter total amount:")
    topentry = Entry(top)

    midlabel = Label(top, text="Output:")
    twok = Label(top, text="2000:")
    twokentry = Entry(top)
    fivehundred = Label(top, text="500:")
    fivehundredentry = Entry(top)
    onehundred = Label(top, text="100:")
    onehundredentry = Entry(top)

    toplabel.pack()
    topentry.pack()

    midlabel.pack()
    twok.pack()
    twokentry.pack()
    fivehundred.pack()
    fivehundredentry.pack()
    onehundred.pack()
    onehundredentry.pack()

    def calculator():
        twokentry.delete(0, END)
        fivehundredentry.delete(0, END)
        onehundredentry.delete(0, END)

        total = int(topentry.get())
        if total % 100 == 0:
            t1 = total//2000
            total %= 2000
            t2 = total//500
            total %= 500
            t3 = total//100
            total %= 100
        else:
            messagebox.showerror("Error", "Value must be divisible by 100")
        
        twokentry.insert(0, str(t1))
        fivehundredentry.insert(0, str(t2))
        onehundredentry.insert(0, str(t3))

    calcbutton = Button(top, text="Calculate!", command=calculator)
    calcbutton.pack(pady=10)


root.mainloop()

    