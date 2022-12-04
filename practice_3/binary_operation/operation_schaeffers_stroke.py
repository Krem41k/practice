from practice_3.operation import Operation


class SchaeffersStroke(Operation):
    def get_name(self):
        return 'Штрих Шеффера'

    def get_symbol(self):
        return '/'

    def get_result(self, a, b):
        y = bin(a & b)
        res = ''
        for i in range(2, len(y)):
            if y[i] == '1':
                res = res + '0'
            else:
                res = res + '1'
        return int(res, 2)
