import random

class Person():

    def __init__(self, name, surname):

        self.name = name
        self.surname = surname

    def __str__(self):

        return('Person "{}, {}"'.format(self.name, self.surname))


    def say_hi(self):

        random_number = random.randint(0,2)

        if(random_number == 0):
            print('Buongiorno, sono {} {}'.format(self.name, self.surname))
        elif(random_number == 1):
            print('Ei, sono {} {}'.format(self.name, self.surname))
        elif(random_number == 2):
            print('Ei bro! sono {} {}'.format(self.name, self.surname))

class Student(Person): 

    def __str__(self):
        return('Student "{} {}"'.format(self.name, self.surname))


class Professor(Person):

    def __str__(self):
        return('Professor "{} {}"'.format(self.name, self.surname))

    def say_hi(self):
        print('Buongiorno , sono il Professor {} {}'.format(self.name, self.surname))
    

person = Person('Mario','Rossi')
print (person)
person.say_hi()
student = Student('Michela', 'Parisini')
print(student)
student.say_hi()
professor = Professor('Luigi', 'Bianchi')
print(professor)
professor.say_hi()

