def quick_sort(user_input):
    #0,3,2,5,4 -> sample input
    lower_items = []
    higher_items = []
    equal_items = []
    if len(user_input) <= 1:
        return user_input
    #pick a pivot and sort out numbers to the left and right of it 
    else:
        pivot = user_input.pop()
    #pivot = last number

    #if i of number < pivot, put in a list
    for i in user_input:
        if i < pivot :
            lower_items.append(i)
        
        elif i == pivot:
            equal_items.append(i)

    #if i of number > pivot, put in another list
        else:
            higher_items.append(i)

    #to print the sorted input, nums in lower_list + pivot + nums in greater_list
    return quick_sort(lower_items) + [pivot] + quick_sort(equal_items) + quick_sort(higher_items)
user_input = [5,6,7,8,9,8,7,6,7,8,9,0]
print(quick_sort(user_input))