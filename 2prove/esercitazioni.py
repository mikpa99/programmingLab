my_list = [12, 3, 6, 15, 9]
my_stringa = 'ciao'
print('la mia stringa è: {}'.format(my_stringa))

for item in my_list:
    if item < 10:
        print(item)
    else:
        item = -item
        print(item)

my_stringa2 = 'buongiorno come stai'
print(my_stringa2[0:15])

my_list2 = ['marco', 'paolo', 'stefano']

i = 1
while(i<20):
    a = i*i
    print(i+i)
    i = i+2

print('------')

for i in range(5):
    print(i)

def eleva_al_quadrato( numero):
    n = numero * numero
    return (n)
    
m = 5
n = eleva_al_quadrato(m)
print('il quadrato di {} è {}'.format(m, n)) 

print('dizionari')
my_dict = {'michela': 23, 'anna' : 34, 'stefania' : 25, 'luca' : 36 }
print(my_dict)
if 'michela' in my_dict:
    print('l età di michela è: {}'.format(my_dict['michela']))

for i, item in enumerate(my_list):
    print('in posizione {} abbiamo {}'.format(i, item))

def fattoriale(n):
    fatt = 1
    if(n == 0):
        return fatt
    elif(n == 1):
        return fatt
    else:
        return n * fattoriale(n-1)
    
fatt = fattoriale(m)
print('il fattoriale di {} è {}'.format(n, fatt))

b = 1
for i in range(m-1):
    b = b * (m)
    m = (m-1)
print('il fattoriale iterativo è {}'.format(b))

my_super_list = [1, 2, 4, 6, 5, 7, 1, 8, 9]

def quanti_elementi(my_list):
    elem = 0
    for item in my_list:
        elem = elem + 1
    return elem
    

        
print(my_super_list)
print('gli elementi sono {}'.format(quanti_elementi(my_super_list)))

    
