class Employee:
    def __init__(self,Name,id):
        self.Name = Name
        self.id = id
    def Info(self):
        print("Employee Name is: ",self.Name)
        print("Id is",self.id)

class JuniorEmployee(Employee):
    def __init__(self,Name,id,project_count,Performance_Score):
        Employee.__init__(self,Name,id)
        self.count = project_count
        self.score = Performance_Score
    def Info(self):
        Employee.Info(self)
        print("Project Count is: ",self.count)
        print("Performace Score is: ",self.score)



class SeniorEmployee(JuniorEmployee):
    def __init__(self,Name,id,project_count,Performance_score,Experience,):
        JuniorEmployee.__init__(self,Name,id,project_count,Performance_score)
        self.Experience = Experience
    def Info(self):
        Employee.Info(self)
        JuniorEmployee.Info(self)
        print("The Experience of ",self.Experience," Years")


Vegash = Employee("Vegash",1234)
Vegash.Info()
Eniya = JuniorEmployee("Eniya",4567,5,"76%")
Eniya.Info()
Kashif = SeniorEmployee("Kashif",4563,12,"88%",5)
Kashif.Info()

print(SeniorEmployee.__mro__)