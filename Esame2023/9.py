class ExamException(Exception):
    pass

my_file = open('dati_sbagliati.csv', 'r')

my_time_series = [line for line in my_file if not 'date' in line]
print(my_time_series)

my_list_b = my_time_series[:]

ordered_and_not_dulicated = True
same = True

my_list_b.sort()

for i in range(len(my_time_series)):
    if my_time_series[i] != my_list_b[i]:
        same = False

if not same  or len(my_time_series) != len(set(my_list_b)):
    ordered_and_not_dulicated = False

if not ordered_and_not_dulicated: 
    
    raise ExamException('il file presenta duplicati o non è ordinato')
