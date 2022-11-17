import random
import operator
from employee import Employee

FILENAME = r".\\output_file.txt"
names = ['Иван', 'Пётр', 'Василий', 'Даниил', 'Илья', 'Дмитрий', 'Станислав', 'Владислав', 'Сергей', 'Павел']
positions = ['Инженер-программист', 'Ведущий инженер-программист', 'Программист', 'Старший инженер-программист',
             'Электроник', 'Инженер-электроник', 'Старший инженер-электроник', 'Ведущий инженер-электроник',
             'Технический писать', 'Тестировщик']
COUNT_PEOPLES = 10
sort_parameter = 'age'
is_descending = True


def create_employee(name: str, salary: int, position: str,
                    weight: float, height: float, age: int):
    return Employee(name, salary, position, weight, height, age)


def create_list_employers():
    list_employers = []

    for i in range(COUNT_PEOPLES):
        employee = create_employee(name=random.choice(names), salary=random.randint(20_000, 100_000),
                                   position=random.choice(positions), weight=random.uniform(65.0, 100.0),
                                   height=random.uniform(1.65, 2.0), age=random.randint(18, 65))
        list_employers.append(employee)

    return list_employers


def write_list_employers(list_employers):
    with open(FILENAME, "w", encoding="utf8") as file:
        [file.write(str(employee)) for employee in list_employers]


if __name__ == '__main__':
    employers = create_list_employers()
    employers.sort(key=operator.attrgetter(sort_parameter), reverse=is_descending)
    print(*employers)
    write_list_employers(employers)
