import random
import operator
from practice_1.employee import Employee

# название файла вывода
FILENAME = r".\\output_file.txt"
# список имён для создания объектов
names = ['Иван', 'Пётр', 'Василий', 'Даниил', 'Илья', 'Дмитрий', 'Станислав', 'Владислав', 'Сергей', 'Павел']
positions = ['Инженер-программист', 'Ведущий инженер-программист', 'Программист', 'Старший инженер-программист',
             'Электроник', 'Инженер-электроник', 'Старший инженер-электроник', 'Ведущий инженер-электроник',
             'Технический писать', 'Тестировщик']
# количество создаваемых объектов
COUNT_PEOPLES = 10
# атрибут сортировки
sort_parameter = 'height'
# параметр сортировки по убыванию или возрастанию
is_descending = False


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


def practice_1(sort_param=sort_parameter, is_desc=is_descending):
    employers = create_list_employers()
    employers.sort(key=operator.attrgetter(sort_param), reverse=is_desc)
    print(*employers)
    write_list_employers(employers)
