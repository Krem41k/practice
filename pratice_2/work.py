from tkinter import *


def work():
    def clicked():
        res = 'Привет {}'.format(txt.get())
        lbl.configure(text=res)

    window = Tk()

    window.title('Добро пожаловать в приложение Python')
    window.geometry('500x350')

    lbl = Label(window, text='Привет')
    lbl.grid(column=0, row=0)

    txt = Entry(window, width=10)
    txt.grid(column=1, row=0)

    btn = Button(window, text='Жми!', command=clicked)
    btn.grid(column=2, row=0)

    window.mainloop()



