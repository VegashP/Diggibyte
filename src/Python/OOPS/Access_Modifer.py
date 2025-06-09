#Private Variables and Methos (Use Double Underscore)
class Login:
    def __init__(self,User_Name, Password):
        self.UserName = User_Name
        self.__Password = Password
    def __Info(self):
        print(f"Its Private Method")

Person = Login("Sam","34")
print(Person.UserName)
# Person.PassWord -> Error Because Its Private Variable
# Person.Inf0     -> Error Because Its Private Methos



#Protected
'''
It can Access by its Class, Method and its SubClass
Using Object, We Can Access it (Not Recommanded)
'''
class Login_02:
    def __init__(self,UserName,Password):
        self._UserName = UserName
        self._Password = Password

class Appication(Login_02):
    def Info(self):
        print(f"User Name is {self._UserName} and The Password is {self._Password}") # Here It Allow to Use

Obj = Appication("Sam","123")
print(Obj._UserName)  # Here We can Able to use but Not Good Practice to use (Not Recommanded)




# Public  ->  We Can access Anywhere
class Login_03:
    def __init__(self, UserName, Password):
        self._UserName = UserName
        self._Password = Password
Obj_02 = Login_03("Ram","345")
