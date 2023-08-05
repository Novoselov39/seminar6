def f(a,b,c):
    list=[a]
    for i in range(1,c):
        list.append(list[i-1]+2)
    return list

print(f(7,2,5))