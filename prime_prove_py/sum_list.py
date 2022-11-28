def sum_list(my_list):
    somma = 0
    for item in my_list:
        somma += item
    return somma
        
my_list = [1, 2, 3, 4, 5]
somma = sum_list(my_list)
print('la somma di my_list {} è {}'.format(my_list, somma))
