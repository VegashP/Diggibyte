class Customer:
    def __init__(self,Customer_Name,Customer_Id):
        self.Customer_name = Customer_Name
        self.Customer_Id = Customer_Id
    def Info(self):
        print("The Customer Name is: ",self.Customer_name)
        print("The Customer Id is: ",self.Customer_Id)


class Order:
    def __init__(self,Order_name,Order_Id,Location):
        self.name = Order_name
        self.id = Order_Id
        self.location = Location
    def Info(self):
        print("The Item name is",self.name)
        print("the Item Id is", self.id)
        print("The Location is: ", self.location)


class OnlineOrder(Customer,Order):
    def __init__(self,Customer_Name,Customer_Id,Order_name,Order_Id,Location):
        Customer.__init__(self,Customer_Name,Customer_Id)
        Order.__init__(self,Order_name,Order_Id,Location)
    def Info(self):
        Customer.Info(self)
        Order.Info(self)

Chicken = OnlineOrder("Vegash",123,"Chicken",9876,"Bangalore")
Chicken.Info()