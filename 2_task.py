def f(list_1,min,max):
    list_2=[]
    for i in range(len(list_1)):
        if list_1[i]>=min and list_1[i]<=max:
            list_2.append(i)
    return(list_2)
        

print(f([1,2,3,6,7],2,7))