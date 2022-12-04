from practice_3.operation import Operation


class And(Operation):
    def get_name(self):
        return 'И'

    def get_symbol(self):
        return '&'

    def get_result(self, a, b):
        return a & b
