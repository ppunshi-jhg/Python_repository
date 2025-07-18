class Animal:
    def __init__(self, name):
        self.name = name
    def speak(self):
        print("Generic Sound!")
        
class Dog(Animal):
    def speak(self):  #Here, we're overriding the method of main class speak, because whenever we create instance of this class and call the speak method- first it calls the speak method of Dog class for which instance has been created
        print("Woof")
        
class Cat(Animal):
    def speak(self):
        print("Meow")
        
my_dog = Dog("Rover")  #It calls the main class constructor and assign rover name to it
my_cat = Cat("Fluffy")

print(my_dog.name)
print(my_cat.name) 

#They both have a name attribute (inherited from Animal)

print(my_dog.speak())
print(my_cat.speak())

# They both have a 'speak' method, but it behaves differently:

#But lets say if you want to call the parent class method as well along with the child class method

#Use super() method inside the child class