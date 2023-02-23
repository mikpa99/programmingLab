class ExamException(Exception):
    pass

my_file = open('dati_sbagliati.csv', 'r')

my_list = [line for line in my_file if not 'date' in line]
print(my_list)

my_list_b = my_list[:]

ordered_and_not_dulicated_list = True
same = True

my_list_b.sort()

for i in range(len(my_list)):
    if my_list[i] != my_list_b[i]:
        same = False

if not same  or len(my_list) != len(set(my_list_b)):
    ordered_and_not_dulicated_list = False

if not ordered_and_not_dulicated_list: 
    
    raise ExamException('il file presenta duplicati o non è ordinato')
