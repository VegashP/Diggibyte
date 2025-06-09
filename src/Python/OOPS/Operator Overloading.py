class imagnation_number:
    def __init__(self,first,second):
        self.first = first
        self.second = second
    def __add__(self, other):
        return f"{self.first + other.first} + {self.second+other.second}i"


P1 = imagnation_number(2,4)
P2 = imagnation_number(6,8)

print(P1+P2)


