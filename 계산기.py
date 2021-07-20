from tkinter import*


window=Tk()
window.geometry("300x400")
window.title("계산기")

entry=Entry(window, width=25)
entry.place(x=40,y=20)
entry.insert(0,"")

def btn_press(num):
    num2= entry.get()
    entry.delete(0, END)
    entry.insert(0, str(num2) + str(num))

def operator_press(op):
    global operator
    operator=op
    entry.insert(END,str(op))


def equal_press():
    a=entry.get()
    res=eval(a)
    entry.delete(0, END)
    entry.insert(0,str(res))

def clear_press():
    entry.delete(0,END)

button0=Button(window, text='0', padx=15, pady=10,command=lambda :btn_press(0))
button1=Button(window, text='1', padx=15, pady=10,command=lambda :btn_press(1))
button2=Button(window, text='2', padx=15, pady=10,command=lambda :btn_press(2))
button3=Button(window, text='3', padx=15, pady=10,command=lambda :btn_press(3))
button4=Button(window, text='4', padx=15, pady=10,command=lambda :btn_press(4))
button5=Button(window, text='5', padx=15, pady=10,command=lambda :btn_press(5))
button6=Button(window, text='6', padx=15, pady=10,command=lambda :btn_press(6))
button7=Button(window, text='7', padx=15, pady=10,command=lambda :btn_press(7))
button8=Button(window, text='8', padx=15, pady=10,command=lambda :btn_press(8))
button9=Button(window, text='9', padx=15, pady=10,command=lambda :btn_press(9))
buttonadd=Button(window, text='+', padx=15, pady=10,command=lambda :operator_press("+"))
buttonsub=Button(window, text='-', padx=15, pady=10,command=lambda :operator_press("-"))
buttonmul=Button(window, text='x', padx=15, pady=10,command=lambda :operator_press("x"))
buttondiv=Button(window, text='/', padx=15, pady=10,command=lambda :operator_press("/"))
buttonequ=Button(window, text='=', padx=15, pady=10,command=lambda :equal_press())
buttonc=Button(window, text='C', padx=15, pady=10,command=lambda :clear_press())

button0.place(x=80,y=200)
button1.place(x=30,y=150)
button2.place(x=80,y=150)
button3.place(x=130,y=150)
button4.place(x=30,y=100)
button5.place(x=80,y=100)
button6.place(x=130,y=100)
button7.place(x=30,y=50)
button8.place(x=80,y=50)
button9.place(x=130,y=50)
buttonadd.place(x=180,y=50)
buttonsub.place(x=180,y=100)
buttonmul.place(x=180,y=150)
buttondiv.place(x=180,y=200)
buttonequ.place(x=130,y=200)
buttonc.place(x=30,y=200)


window.mainloop()