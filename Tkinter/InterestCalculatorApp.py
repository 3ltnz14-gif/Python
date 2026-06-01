from tkinter import *

window = Tk()
window.geometry("400x300")
window.title("Interest Calculator App")

amount_label = Label(window, text = "Amount:")
amount_label.pack(pady = 10)
amount_entry = Entry(window)
amount_entry.pack(pady = 5)

time_label = Label(window, text = "Time (in years):")
time_label.pack(pady = 10)
time_entry = Entry(window)
time_entry.pack(pady = 5)

rate_label = Label(window, text = "Interest Rate (%)")
rate_label.pack(pady = 10)
rate_entry = Entry(window)
rate_entry.pack(pady = 5)

def calculate():
    amount = float(amount_entry.get())
    time = float(time_entry.get())
    rate = float(rate_entry.get())
    interest = (amount * time * rate) / 100
    interest_label.config(text = interest)

interestbutton = Button(window, text = "Calculate Interest", command = calculate)
interestbutton.pack(pady = 10)

interest_label = Label(window, text = "Simple Interest: ")
interest_label.pack(pady = 5)

window.mainloop()