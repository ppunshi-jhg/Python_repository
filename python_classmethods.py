# Class Methods: That is bound to class and not the instance of the class.To define a class method- you need to put class decorator before the method defined.

class Employee:
    company="Apple"  #This is the class variable
    def show(self):
        print(f"The name is {self.name} and company is {self.company}")
        
    def changeCompany(self,newCompany):
        self.company=newCompany
        
e1=Employee()
e1.name="Prince"
e1.show()

