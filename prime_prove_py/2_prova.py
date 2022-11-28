my_dict = {'michela': 23, 'noa':22, 'meryem': 24}
for item in my_dict:
    print('gli anni di {} sono: {}'.format(item, my_dict[item]))

my_var = 59
your_var = 44.5
if (my_var > your_var):
    print('my var is bigger than yours')
    if (my_var - your_var < 2):
        print('...not so much')
    elif (my_var - your_var < 5):
        print('...quite a bit')
    else:
        print('...a lot!')

def my_funct(x,y):
    print('le mie variabili sono {} e {}'.format(x, y))

my_funct(my_var, your_var)

for i in range(10):
    print(i)

my_list = ['sofia', 'anna', 'irene', 'sara']
for i, item in enumerate(my_list):
    print('posizione: {}, contenuto:{}'.format(i, item))

def eleva_quadrato(x):
    return x*x

quadrato = eleva_quadrato(my_var)
print('il quadrato di {} è {}'.format(my_var, quadrato))