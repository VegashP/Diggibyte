from abc import ABC,abstractmethod
from idlelib.debugger_r import close_subprocess_debugger


def Car(ABS):
    @abstractmethod
    def Engine(Self):
        pass

    @abstractmethod
    def Weight(ABS):
        pass


class Audi:
    def __init__(self,color,price):
        self.color = color
        self.price = price
    def Engine(self):
        print("Type of Fuel is Petrol")
        print("The Capcity is 4 Litres")
    def Weight(self):
        print("The Weight is 1 tone")



class BMW:
    def __init__(self,color,price):
        self.color = color
        self.price = price
    def Engine(self):
        print("Type of Fuel is Diesel")
        print("The Capcity is 6 Litres")
    def Weight(self):
        print("The Weight is 2 tone")


print("Audi Models")
Aud_Model_01 = Audi("Red",1000000)
Aud_Model_01.Engine()
Aud_Model_01.Weight()
print("***********************************************************")
print("BWM Models")
BWM_Model_01 = BMW("Black",200000)
Aud_Model_01.Engine()
Aud_Model_01.Weight()
