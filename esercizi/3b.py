import random

class Person():

    def __init__(self, name, surname, age):

        self.name = name
        self.surname = surname
        self.age = age

    def __str__(self):
        return('Person "{} {} {}"'.format(self.name, self.surname, self.age))

    def say_hi(self):
        a = random.randint(0,1)

        if(a == 0):
            print('ciao sono {} {} ed ho {} anni'.format(self.name, self.surname, self.age))
        elif(a == 1):
            print('Ehilà sono {}'.format(self.name))

def somma_età(self, person, person1):
    return(person.self.age + person1.self.age)
    

person = Person('Mario', 'Rossi', '52')
print(person)
person.say_hi()
person1 = Person('Lucia', 'Luciani', '27')
print(person1)
person1.say_hi()
my_var = '12'
my_var = float(my_var)
new_var = my_var + 2
print(new_var)