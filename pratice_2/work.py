from tkinter import *
from tkinter.messagebox import showinfo, showerror

welcome_line = 'Здесь можно вычислит длительность выплат в зависимости от: ' \
               'суммы кредита, годового процента и ежемесечной выплаты'
please_line = 'Внесите данные:'
sum_credit = 'Сумма кредита = '
year_percent = 'Годовой процент = '
monthly_payment = 'Ежемесечная выплата = '

note = 'Заполните ячейки значениями'


def work():
    def isfloat(num):
        try:
            float(num)
            return True
        except ValueError:
            return False

    def isint(num):
        try:
            float(num)
            return True
        except ValueError:
            return False

    def check_values(sum, percent, payment):
        if isfloat(sum):
            sum = float(sum)
        elif isint(sum):
            sum = int(sum)
        else:
            showerror(title="Информация", message='Неккоректный тип данных')

        if isfloat(percent):
            percent = float(percent)
        elif isint(percent):
            percent = int(percent)
        else:
            showerror(title="Информация", message='Неккоректный тип данных')

        if isfloat(payment):
            payment = float(payment)
        elif isint(payment):
            payment = int(payment)
        else:
            showerror(title="Информация", message='Неккоректный тип данных')

        return sum, percent, payment

    def calculate():
        sum, percent, payment = check_values(sum_value.get(), percent_value.get(), payment_value.get())

        count = 0
        while sum >= 0:
            if percent > payment:
                break
            sum += sum * (percent / 100)
            sum -= payment
            count += 1

        if count == 0:
            message = 'Невозможно погасить кредит'
        else:
            message = f'Количество месяцев для погашения: {count}'

        showinfo(title="Информация", message=message)

    def clear():
        sum_value.delete(0, END)
        percent_value.delete(0, END)
        payment_value.delete(0, END)

    window = Tk()

    window.title('Добро пожаловать в графическое приложение Python')
    window.geometry('920x200')

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

    btn_calculate = Button(window, text='Рассчитать!', height=3, width=10, command=calculate)
    btn_calculate.place(x=400, y=65)

    btn_clear = Button(window, text='Очистить!', height=3, width=10, command=clear)
    btn_clear.place(x=600, y=65)

    note_label = Label(window, text=note, font="Arial 14")
    note_label.place(x=0, y=145)

    window.mainloop()
