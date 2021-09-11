from main import StackExample

#def is_match, to check if the brackets are equal
def is_match(p1, p2):
    if p1 == "(" and p2 == ")":
        return True
    elif p1 == "[" and p2 == "]":
        return True
    elif p1 == "{" and p2 == "}":
        return True
    else:
        return False

#def balanced_brackets to check for equality or not
def balanced_brackets(brackets):
    m = StackExample()
    bra_index = 0
    is_balanced = True

    #while loop
    while bra_index < len(brackets) and is_balanced:
        bracket = brackets[bra_index]
        if bracket in "{[(":
            new = m.push(bracket)
        
        else:
            if m.is_empty():
                is_balanced = False
                break
            else:
                remove = m.pop()
                if not is_match(remove, bracket):
                    is_balanced = False
                    break
        bra_index += 1
    if m.is_empty and is_balanced:
        print(True)
    else:
        print(False)

balanced_brackets("[)")