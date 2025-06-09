class Login_Page:
    def __init__(self,Name,Age,Gender):
        self.Name = Name
        self.__Age = Age
        self.__Gender = Gender
    def get_age(self):
        return self.__Age
    def get_gender(self):
        return self.__Gender

    def set_age(self,age):
        self.__Age = age
    def set_gender(self,gender):
        self.__Gender = gender


Vegash = Login_Page("Vegash",21,"Male")
Vegash.set_age(22)
print(Vegash.get_gender())
print(Vegash.get_age())