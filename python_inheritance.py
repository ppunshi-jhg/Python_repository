class Employee:
    def __init__(self,name,occupation):
        self.name=name
        self.occupation=occupation
    
    def info(self):
        print(f"Employee name is {self.name} and occupation is {self.occupation}")
        
class Programmer(Employee):
    # You dont need to define the constructor in the inherited class, but when you make the instanceof the inherited class you need to pass the number of arguments which parent class needs- but if you pass the constructor you need to have at least same number of arguments as parent class and you can add more.
    def __init__(self,name,occupation,age):
        super().__init__(name,occupation)
        self.age=age
    def infoProgrammer(self):
        print(f"He is programmer: {self.name} and age is {self.age}")
        
p=Programmer("Prince","Se",29)
p.infoProgrammer()
