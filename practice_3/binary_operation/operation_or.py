from practice_3.operation import Operation


class Or(Operation):
    def get_name(self):
        return 'ИЛИ'

    def get_symbol(self):
        return '|'

    def get_result(self, a, b):
        return a | b
