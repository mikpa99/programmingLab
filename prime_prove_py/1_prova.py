number_list = [1, 3, 67, 5, 35, 40]
for item in number_list:
    if item % 5 == 0:
        print(item)

print('i valori di number_list sono {}'.format(number_list))

my_var_1 = 30
my_var_2 = 45
if my_var_1 <= my_var_2:
    my_var_2 = my_var_2 - my_var_1
    print('{}'.format(my_var_2))

mia_stringa = 'buongiorno'
print('{}'.format(mia_stringa[0:5]))
print('{}'.format(mia_stringa[5:-1]))

my_list = ['marta','carlo', 'genoveffa']
print('my_list è {}'.format(my_list))
for item in my_list:
        print('{}'.format(item))

sec_list = ['marta', 1, 3]
print('sec_list è {}'.format(sec_list))


