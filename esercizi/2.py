import random

class Person():

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def __str__(self):
        return 'Person "{} {}"'.format(self.name, self.surname)

    def say_hi(self):
        
        random_number = random.randint(0,2)
        print('{}'.format(random_number))
        
        if(random_number == 0):
            print('hey Bro, {} here!'.format(self.name))
        elif(random_number == 1):
            print('hi, i am {} {}'.format(self.name, self.surname))
        elif(random_number == 2):
            print('Hello, i am {} {}'.format(self.name, self.surname))

person = Person('Mario' , 'Rossi')
person.say_hi()