#Classes are User Defined Data Type
#Eg:
from itertools import count


class Obj:
    pass
OBJ = Obj()
print(Obj)

#1. __init__ (Constructor)
class Emp:
    def __init__(self,Name,Age):
        self.Name = Name
        self.Age = Age
Vegash = Emp("Vegash",21)
print(Vegash.Name)
print(Vegash.Age)


#2. Class Variable
class Emp_01:
    count = 0
    def __init__(self):
        Emp_01.count += 1
Sam = Emp_01()
Ram = Emp_01()
print(Emp_01.count)

#3. Method in Classes
class Emp_02:
    def __init__(self, Name, Age):
        self.Name = Name
        self.Age = Age

    def DisplayName(self):
        print(self.Name)

    def DisplayAge(self):
        print(self.Age)

    def Id(self, Id):
        print("Okay Your Emp_Id is",Id)
Sam = Emp_02("Sam",22)
Sam.Id(55)



#4. Instance Methods, Class Methods, Static Methods
class Emp_03:
    def fun(Method):
        print("Class method")
    def fun(self):
        print('Instance Method')
def fun():
    print("Static method")

Ram = Emp_03()
Ram.fun()
Emp_03.fun(Emp_03)
fun()