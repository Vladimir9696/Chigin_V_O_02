from tkinter import *
from main3 import word_to_number
root = Tk()
root.geometry('400x250')


def btn_click():
    number = number_input.get()
    text = word_to_number(number)
    info['text'] = text



frame = Frame(root, bg='#ada0a0')
frame.place(relx=0, rely=0, relwidth=1, relheight=1)

number_input = Entry(frame, bg='white', font=('Arial', 15), width=35)
number_input.pack()

btn = Button(frame, text='Ввод', command=btn_click)
btn.pack()

info = Label(frame, text='Результат')
info.pack()

root.mainloop()
