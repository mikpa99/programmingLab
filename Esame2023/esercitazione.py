my_file = open('data.csv', 'r')
my_list = []

for line in my_file:
    #itero tutte le line del mio file
    element = line.split(',') 
    #separo gli elementi della line
    element[1] = element[1].strip()
    #pulisco eventuali caratteri inutili
    
    if element[0] != 'date': 
        date = element[0]
        date = date.split()
        #controllo che non passo l'intestazione
        element[1] = float(element[1])
        #converto il valore in float
        my_list.append(element, year, )
        #aggiungo elemento alla lista che conterrà i valori

#stampo la mia lista
for element in my_list:
    print (element)

#sommo 
sum = 0
for value in my_list:
    sum += value[1]

print(sum)


my_file.close()