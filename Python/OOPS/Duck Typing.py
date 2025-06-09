#Example:
class son:
    def __init__(self,Name,Age):
        self.Name = Name
        self.Age = Name
    def Passion(self):
        print(f"{self.Name} Passsion is to Become Engineer")

class father:
    def __init__(self, Name, Age):
        self.Name = Name
        self.Age = Name
    def Passion(self):
        print(f"{self.Name} Passsion is to Become Engineer")

class grandfather:
    def __init__(self, Name, Age):
        self.Name = Name
        self.Age = Name
    def Passion(self):
        print(f"{self.Name} Passsion is to Become Engineer")


def Interest(self):
    self.Passion()


sam = son("Son",21)
ram = father("Ram",45)
Dhinesh = grandfather("Dhinesh",85)


Interest(sam)
Interest(ram)
Interest(Dhinesh)
