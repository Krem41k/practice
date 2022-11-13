from employee import Employee


def create_employee(name: str, salary: int, position: str,
                    weight: float, height: float, age: int):
    return Employee(name, salary, position, weight, height, age)


def create_list_employers():
    list_employers = []
    employee = create_employee(name='Иван', salary=50000, position='Инженер-программист',
                               weight=70.5, height=1.84, age=27)
    list_employers.append(employee)
    return list_employers


if __name__ == '__main__':
    employers = create_list_employers()
    print(*employers)
