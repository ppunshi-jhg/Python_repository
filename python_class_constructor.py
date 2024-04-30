
# Constructor- is a function which gets called whenever you create an instance of the class and it needs to be made on the top after defined the class and you can pass argumments to your constructor and it can be passed whenever an instance is created.

class Person:
    # def __init__(self):
    #     print("Hey I'm called")
    def __init__(self,name,age):
        self.name=name  #self refer to an object of Person class and name and age passed as an arguments are temp variable, but self.name means the name of the object has been set to the passed argument- you can have self.name1, self.name2 but make sure you pass the same variable like name 1 in the info method
        self.age=age
    def info(self):
        print(f"My name is {self.name} and my age is {self.age}")
        


p=Person("Prince",29)
p.info()
