class Employee:
    def __init__(self,name,occupation):
        self.name=name
        self.occupation=occupation
        
    def info(self):
        print(f"Employee name is {self.name} and occupation is {self.occupation}")
        
class Programmer(Employee):
    def infoProgrammer(self):
        print(f"He is programmer: {self.name}")
        
p=Programmer()
p.infoProgrammer()