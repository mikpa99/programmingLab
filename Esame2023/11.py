my_file = open('dati_sbagliati.csv', 'r')

for line in my_file:
    
    element = line.split(',')
    if len(element) < 2:
        continue
    
    my_list = []
    my_list.append(element)
    print(my_list)