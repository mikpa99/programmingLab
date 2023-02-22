import math

class FigureGeometriche():

    def perimetro(self):
        pass

    def area(self):
        pass

class Rettangolo(FigureGeometriche):

    def __init__(self, base, altezza):
        self.base = base
        self.altezza = altezza

    def __str__(self):
        return ('Rettangolo {} {}'.format(self.base, self.altezza))

    def tipo(self):
        if(self.base == self.altezza):
            print('è un quadrato')
        else:
            print(' è un rettangolo')

    def perimetro(self):
        super().perimetro()
        return (self.base + self.altezza)*2

    def area(self):
        super().area()
        self.base = float(self.base)
        self.altezza = float(self.altezza)
        return ((self.base) * (self.altezza))

class Triangolo(FigureGeometriche):

    def __init__(self, lato_1, lato_2, lato_3):
        self.lato_1 = lato_1
        self.lato_2 = lato_2
        self.lato_3 = lato_3

    def tipo(self):
        if(self.lato_1 == self.lato_2 == self.lato_3):
            print('è un triagolo equilatero')
        elif(self.lato_1 != self.lato_2 != self.lato_3):
            print('il triangolo è scaleno')
        else:
            print('il triangolo è isoscele')


    def perimetro(self):
        super().perimetro()
        return (self.lato_1+ self.lato_2+ self.lato_3)/2


    def area(self):
        super().area()
        return math.sqrt(self.perimetro * (self.perimetro- self.lato_1)-(self.perimetro- self.lato_2)-(self.perimetro- self.lato_3))


class Cerchio(FigureGeometriche):

    def __init__(self, raggio):
        self.raggio = raggio

    def area(self):
        super().area()
        return (self.raggio)^2*3,14

    def perimetro(self):
        super().perimetro()
        return (self.raggio + self.raggio)*3.14


def sommaaree(self, triangolo , rettangolo):
    return (triangolo.area()+rettangolo.area())


rettangolo = Rettangolo('2', '2')
print(rettangolo)
print(rettangolo.area())

        

    
