from practice_3.operation import Operation


class Xor(Operation):
    def get_name(self):
        return 'Исключающее ИЛИ'

    def get_symbol(self):
        return '^'

    def get_result(self, a, b):
        return a ^ b
