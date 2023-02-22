list1 = [ 122, 32, 67, 90, 20, 18]
list2 = [100, 15, 6, 80, 4, 6]
list = [abs(list1[i]- list1[i+1]) for i in range(len(list1)-1)]

listi = [abs(list2[i]- list2[i+1]) for i in range(len(list2)-1)]

print(list)
print(listi)

similar = [-2, -1, 0, 1, 2, 5]
    
try:
    return_list = [True if list[i]-listi[i] in similar else False for i in range(len(list))] 

except Exception as e:
    print('ho avuto un errore "{}"'.format(e))

print(return_list)
    
