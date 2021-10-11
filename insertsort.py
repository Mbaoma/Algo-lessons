def insertion_sort(sequence):
    #start from the curr number at 1th index, 
    current_number = range(1, len(sequence))

    #compare it to the number at the index-1 position
    for i in current_number:
        value_to_sort = sequence[i]
    
    #if the current number > number at index-1, and lesser than 0 -> we can use a loop for this
        while sequence[i-1] > value_to_sort and i > 0:
            
    #switch them both
            sequence[i], sequence[i-1] = sequence[i-1], sequence[i]
            i -= 1
    return sequence

    #reduce the count of i, to keep checking against nums on the left hand side

sequence = [5,6,7,8,9,8,7,6,7,8,9,0]
print(insertion_sort(sequence))