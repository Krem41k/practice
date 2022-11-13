class Employee:
    def __init__(self, name: str, salary: int, position: str,
                 weight: float, height: float, age: int):
        self.verify_name(name)
        self.verify_salary(salary)
        self.verify_position(position)
        self.verify_weight(weight)
        self.verify_height(height)
        self.verify_age(age)

        self.__name = name
        self.__salary = salary
        self.__position = position
        self.__weight = weight
        self.__height = height
        self.__age = age

    def __str__(self):
        return f'Имя сотрудника: {self.name}, зарплата: {self.salary}, должность: {self.position}, ' \
               f'вес: {self.weight}, рост: {self.height}, возраст: {self.age},'

    @classmethod
    def verify_name(cls, name):
        if type(name) != str:
            raise TypeError('Имя должно быть строкой')

    @classmethod
    def verify_salary(cls, salary):
        if type(salary) != int:
            raise TypeError('Зарплата должна быть числом')

    @classmethod
    def verify_position(cls, position):
        if type(position) != str:
            raise TypeError('Должность должна быть строкой')

    @classmethod
    def verify_weight(cls, weight):
        if type(weight) != float:
            raise TypeError('Вес должен быть числом с плавающей точкой')

    @classmethod
    def verify_height(cls, height):
        if type(height) != float:
            raise TypeError('Рост должен быть числом с плавающей точкой')

    @classmethod
    def verify_age(cls, age):
        if type(age) != int:
            raise TypeError('Возраст должен быть числом')

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.verify_name(name)
        self.__name = name

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, salary):
        self.verify_salary(salary)
        self.__salary = salary

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, position):
        self.verify_position(position)
        self.__position = position

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, weight):
        self.verify_weight(weight)
        self.__weight = weight

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        self.verify_height(height)
        self.__height = height

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        self.verify_age(age)
        self.__age = age
