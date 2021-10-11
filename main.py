m = [2,3,4,5,6,7]
n = []
for i in range(len(m)):
    if len(m) == 0 or i <= m[-1]:
        m.append(i)
        print(m)
    n.append(i)
    print('b',m)
