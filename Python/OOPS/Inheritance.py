class Bike:
    def __init__(self,color,Bike_No,):
        self.color = color
        self.Bike_No = Bike_No
    def info(self):
        print("Bike Color is",self.color)
        print("Bike Number is",self.Bike_No)

class SuperBike(Bike):
    def __init__(self,color,Bike_No,speed):
        super().__init__(color,Bike_No)
        self.speed = speed
    def info(self):
        super().info()
        print("The max Speed of your Bike is: ",self.speed)
    def Speed(self):
        return self.speed


Honda = Bike("Red","TN54HZ1234")
Honda.info()
Apache = SuperBike("Red","TN345Z12","120KM/P")
Apache.info()
