from tkinter import*
import random

def btn1_click():
    global n1
    n1 = str(random.randint(0, 2))
    button1.configure(text=n1)

def btn2_click():
    global n2
    n2 = str(random.randint(0, 2))
    button2.configure(text=n2)

def btn3_click():
    global n3
    n3 = str(random.randint(0, 2))
    button3.configure(text=n3)

    if n1 == n2 and n2 == n3:
        label.configure(text="success")
    else:
        label.configure(text="fail")

def btn_reset():
    button1.configure(text="0")
    button2.configure(text="0")
    button3.configure(text="0")
    label.configure(text="")

window=Tk()
window.geometry("300x300")
window.title("갬블링 게임")
window.configure(bg="alice blue")

label = Label(window, width="10", text="", justify="center", bg="alice blue", fg="medium slate blue", font=("Bahnschrift SemiBold", 20))

button1 = Button(window, bg="light cyan", bd=0, font=("consolas", 35, "italic"), text="0", command=btn1_click)
button2 = Button(window, bg="light cyan", bd=0, font=("consolas", 35, "italic"), text="0", command=btn2_click)
button3 = Button(window, bg="light cyan", bd=0, font=("consolas", 35, "italic"), text="0", command=btn3_click)
button4 = Button(window, bg="light cyan", bd=0, font=("consolas", 15), width="5", text="reset", command=btn_reset)

label.place(x=73, y=130)
button1.place(x=45, y=30)
button2.place(x=125, y=30)
button3.place(x=205, y=30)
button4.place(x=125, y=180)
window.mainloop()