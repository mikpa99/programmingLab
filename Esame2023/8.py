class Error(Exception):
    pass

my_list = ['1949-02,1', '1950-01,2', '1948-03,3']


list1 = my_list[:]
print(list1)

try:
    my_list.sort()
except Exception as e:
    print('non posso riordinare la lista:{}'.format(e))

print (my_list)
same = True

for i in range(len(my_list)):
    if list1[i] != my_list[i]:
        same = False

print(same)

if not same:
    raise Error('Le liste non sono uguali')
