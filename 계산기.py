from tkinter import*

window = Tk()
window.geometry("400x480")
window.title("계산기")
window.configure(background="lavender blush")

entry = Entry(window, justify='right', relief="groove", bd=0, bg="lavender blush", fg="light coral", font=("Calibri Light",25))
entry.place(x = 40, y = 40)
entry.insert(0,"")

def btn_press(num):
    input = entry.get()
    entry.delete(0, END)
    entry.insert(0, str(input) + str(num))

def clear_press():
    entry.delete(0, END)

def delete_press():
    entry.delete(len(entry.get()) - 1, 'end')


def operator_press(op):
    global num1
    num1 = float(entry.get())
    global operator
    operator = op
    entry.insert(END, str(op))
    entry.delete(0, END)

def equal_press():
    num2 = entry.get()
    entry.delete(0, END)
    if operator == '+':
        entry.insert(0, num1 + float(num2))
    elif operator == '-':
        entry.insert(0, num1 - float(num2))
    elif operator == '*':
        entry.insert(0, num1 * float(num2))
    elif operator == '/':
        entry.insert(0, num1 / float(num2))


button0 = Button(window, relief="ridge", width=4, bd=0, bg="lavender", text='0', padx=25, pady=20, command=lambda :btn_press(0))
button1 = Button(window, relief="ridge", width=4, bd=0, bg="lavender", text='1', padx=25, pady=20, command=lambda :btn_press(1))
button2 = Button(window, relief="ridge", width=4, bd=0, bg="lavender", text='2', padx=25, pady=20, command=lambda :btn_press(2))
button3 = Button(window, relief="ridge", width=4, bd=0, bg="lavender", text='3', padx=25, pady=20, command=lambda :btn_press(3))
button4 = Button(window, relief="ridge", width=4, bd=0, bg="lavender", text='4', padx=25, pady=20, command=lambda :btn_press(4))
button5 = Button(window, relief="ridge", width=4, bd=0, bg="lavender", text='5', padx=25, pady=20, command=lambda :btn_press(5))
button6 = Button(window, relief="ridge", width=4, bd=0, bg="lavender", text='6', padx=25, pady=20, command=lambda :btn_press(6))
button7 = Button(window, relief="ridge", width=4, bd=0, bg="lavender", text='7', padx=25, pady=20, command=lambda :btn_press(7))
button8 = Button(window, relief="ridge", width=4, bd=0, bg="lavender", text='8', padx=25, pady=20, command=lambda :btn_press(8))
button9 = Button(window, relief="ridge", width=4, bd=0, bg="lavender", text='9', padx=25, pady=20, command=lambda :btn_press(9))
buttonAdd = Button(window, relief="ridge", width=4, bd=0, bg="misty rose", text='+', padx=25, pady=20, command=lambda : operator_press('+'))
buttonSub = Button(window, relief="ridge", width=4, bd=0, bg="misty rose", text='-', padx=25, pady=20, command=lambda : operator_press('-'))
buttonMul = Button(window, relief="ridge", width=4, bd=0, bg="misty rose", text='x', padx=25, pady=20, command=lambda : operator_press('*'))
buttonDiv = Button(window, relief="ridge", width=4, bd=0, bg="misty rose", text='/', padx=25, pady=20, command=lambda : operator_press('/'))
buttonEqu = Button(window, relief="ridge", width=4, bd=0, bg="misty rose", text='=', padx=25, pady=20, command=lambda : equal_press())
buttonC = Button(window, relief="ridge", width=4, bd=0, bg="misty rose", text='C', padx=25, pady=20, command=lambda :clear_press())
buttonDel = Button(window, relief="ridge", width=4, bd=0, bg="misty rose", text='DEL', padx=25, pady=20, command=lambda :delete_press())

button0.place(x=115, y=295)
button1.place(x=30, y=230)
button2.place(x=115, y=230)
button3.place(x=200, y=230)
button4.place(x=30, y=165)
button5.place(x=115, y=165)
button6.place(x=200, y=165)
button7.place(x=30, y=100)
button8.place(x=115, y=100)
button9.place(x=200, y=100)
buttonAdd.place(x=285, y=100)
buttonSub.place(x=285, y=165)
buttonMul.place(x=285, y=230)
buttonDiv.place(x=285, y=295)
buttonEqu.place(x=200, y=295)
buttonC.place(x=30, y=295)
buttonDel.place(x=30, y=360)


window.mainloop()