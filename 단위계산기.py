import tkinter
from tkinter import*
from tkinter import ttk

def length_conversion():
    text.delete(1.0, END)
    com = combo.get()
    val = float(entry.get())

    if com == "mm":
        milli = val
        centi = val / 10
        meter = val / 1000
        kilo = val / 1000000
    elif com == "cm":
        milli = val * 10
        centi = val
        meter = val / 100
        kilo = val / 100000
    elif com == "m":
        milli = val * 1000
        centi = val * 100
        meter = val
        kilo = val / 1000
    elif com == "km":
        milli = val * 1000000
        centi = val * 100000
        meter = val * 1000
        kilo = val

    text.insert(END, str(milli) + "mm\n")
    text.insert(END, str(centi) + "cm\n")
    text.insert(END, str(meter) + "m\n")
    text.insert(END, str(kilo) + "km\n")

window = Tk()
window.geometry("300x300")
window.title("단위 변환기")
window.configure(bg="alice blue")

label1 = Label(window, text="값:", bg="lightblue1")
label2 = Label(window, text="단위:", bg="lightblue1")

entry = Entry(window, width=15, justify="center", bd=0)
entry.insert(0, "")


combo = ttk.Combobox(window, width = 15, justify="center")
combo['values'] = ("mm","cm","m","km")

combo.current(0)

text = Text(window, width=30, height=10, relief="ridge", bg="white", bd=0, font="Mondern")

button=Button(window, text="변환", relief="ridge", bg="lightblue1", bd=0, command=length_conversion)

label1.place(x=50, y=20)
label2.place(x=45, y=60)
text.place(x=40, y=100)
button.place(x=230, y=60)
entry.place(x=90, y=20)
combo.place(x=90, y=60)

window.mainloop()