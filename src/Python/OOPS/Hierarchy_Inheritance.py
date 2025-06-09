class Login:
    def __init__(self,Username,Password):
        self.Username = Username
        self.Password = Password



class Facebook(Login):
    def __init__(self,Username,Passwords):
        super().__init__(Username,Passwords)
        print("You're in Facebook")


class Whatapp(Login):
    def __init__(self,Username,Passwords):
        super().__init__(Username,Passwords)
        print("You're in Whatapp")


class Instagram(Login):
    def __init__(self,Username,Passwords):
        super().__init__(Username,Passwords)
        print("You're in Instagram")




Vegash = Facebook("Iam_vsh","******")
Vegash = Whatapp("Iam_vsh","******")
Vegash = Instagram("Iam_vsh","******")