#Super is helpful in calling parent method and their constructor , and modify if you want

class Animal:
    def __init__(self, name):
        self.name = name
        print(f"Animal {self.name} created")
        
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)  #Call the init of super class
        self.breed = breed
        print(f"")
        