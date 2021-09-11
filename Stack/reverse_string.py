#we reverse a string using stack
#push the letters onto a stack
#pop the letters out and we have a reverse string
from main import StackExample

def reverse_string(word):
    n = StackExample()
    is_empty = True

    for i in range(len(word)):
        new_list = n.push(word[i])
    rev_str = " "
    while not n.is_empty():
        rev_str += n.pop()
    return rev_str

print(reverse_string("!evitacudE ot emocleW"))
            

