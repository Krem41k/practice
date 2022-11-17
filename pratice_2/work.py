from tkinter import *

welcome_line = 'Здесь можно вычислить: сумму кредита, годовой процент, ежемесечная выплата, длительность выплат'
please_line = 'Внесите данные:'
sum_credit = 'Сумма кредита = '
year_percent = 'Годовой процент = '
monthly_payment = 'Ежемесечная выплата = '
duration_payments = 'Длительность выплат ='
note = 'Выберите параметр который хотите рассчитать и посставьте там знак вопроса =>?,\nдругие же заполните значениями'

def work():
    def clicked():
        res = 'Привет {}'.format(txt.get())
        lbl.configure(text=res)

    window = Tk()

    window.title('Добро пожаловать в графическое приложение Python')
    window.geometry('775x200')

    for c in range(3):
        window.columnconfigure(index=c, weight=1)
    for r in range(3):
        window.rowconfigure(index=r, weight=1)

    welcome_label = Label(window, text=welcome_line, font="Arial 12")
    welcome_label.place(x=0, y=0)

    please_label = Label(window, text=please_line, font="Arial 12 bold")
    please_label.place(x=0, y=20)

    sum_label = Label(window, text=sum_credit, font="Arial 12")
    sum_label.place(x=0, y=50)
    sum_value = Entry(window, width=10)
    sum_value.place(x=200, y=50)

    percent_label = Label(window, text=year_percent, font="Arial 12")
    percent_label.place(x=0, y=75)
    percent_value = Entry(window, width=10)
    percent_value.place(x=200, y=75)

    payment_label = Label(window, text=monthly_payment, font="Arial 12")
    payment_label.place(x=0, y=100)
    payment_value = Entry(window, width=10)
    payment_value.place(x=200, y=100)

    duration_label = Label(window, text=duration_payments, font="Arial 12")
    duration_label.place(x=0, y=125)
    duration_value = Entry(window, width=10)
    duration_value.place(x=200, y=125)

    btn = Button(window, text='Рассчитать!', height=3, width=10, command=clicked)
    btn.place(x=400, y=65)

    note_label = Label(window, text=note, font="Arial 14")
    note_label.place(x=0, y=145)

    window.mainloop()
