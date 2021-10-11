def binary_sort(target, num):
    start = 0
    moving_index = len(num)

    while start +1  < moving_index:
        difference = moving_index - start
        avg_val = difference // 2
        
        #move to left
        left = (avg_val + start) 
        guess = num[left]

        #check if target equal to guess
        if guess == target:
            return f"{True} : {guess} equal {target}"
        
        #check if target less than guess
        if guess < target:
            moving_index = left
        
        #check if target greater than guess
        if guess > target:
            start = left
    return f"{False}: value {guess} is {target}"

num = [1,2,3,4,5,6,7,8,9,10]
target = 2
print(binary_sort(target, num))