m = [1,2,3,4,5]
n = [1]
for i in range(len(m)-1, 0, -1):
    print(i)
    n.append(n[-1] * m[i])
    print(f'n -> {n}')
