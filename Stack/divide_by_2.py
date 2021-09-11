#print out the binary equivalent of a decimal number
from main import StackExample
def convert_int_to_bin(dec_num):
    #divide numbers by 2
    #push the remainders into a stack
    #pop the remainders into anoher stack

    n = StackExample()
    is_empty = True
    empty_stack = []

    if dec_num == 0:
        return 0

    while dec_num > 0:
        rem = dec_num % 2
        empty_stack = n.push(rem)
        dec_num = dec_num // 2
    rev_dec_num = ''
    while not n.is_empty():
        rev_dec_num += str(n.pop())
    return rev_dec_num

print(convert_int_to_bin(27))
