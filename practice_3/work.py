from practice_3.binary_operation.operation_and import And
from practice_3.binary_operation.operation_or import Or
from practice_3.binary_operation.operation_schaeffers_stroke import SchaeffersStroke
from practice_3.binary_operation.operation_xor import Xor


def work():
    a = 5
    b = 6

    obj_xor = Xor()
    obj_and = And()
    obj_or = Or()
    obj_schaeffers_stoke = SchaeffersStroke()

    operations = [obj_xor, obj_and, obj_or, obj_schaeffers_stoke]

    for i in operations:
        print(f'Binary format: {i.get_name()} \n {bin(a)} {i.get_symbol()} {bin(b)} = {bin(i.get_result(a, b))} ')
        print(f'Usually format: {i.get_name()} \n {a} {i.get_symbol()} {b} = {i.get_result(a, b)} ')
