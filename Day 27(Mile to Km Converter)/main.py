from tkinter import *
windows = Tk()
windows.title("Mile to KM")
windows.minsize(width=200, height=200)
windows.config(padx=20, pady=20)


def convert():
    in_mile = textbox.get()
    in_km = 1.609 * float(in_mile)
    label3.config(text=round(in_km, 2))



textbox = Entry(width=10)
textbox.grid(row=0, column=1)

label1 = Label(text="Miles")
label1.grid(row=0, column=2)

label2 = Label(text="is equal to")
label2.grid(row=1, column=0)

label3 = Label(text=0)
label3.grid(row=1, column=1)

label4 = Label(text="Km")
label4.grid(row=1, column=2)

button = Button(text="Calculate", command=convert)
button.grid(row=2, column=1)

windows.mainloop()