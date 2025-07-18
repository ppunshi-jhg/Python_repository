#Class is a blueprint and we create instances(object) of the class to make our job easier
#Four pillars of OOPS- Abstraction, Encapsulation, Inheritance, Polymorphism
class Dog:
    species = "Canis" #Class Attribute
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
    
# Whenever we define class we can initialise construtor with some arguments and these arguments can be setupp with the help of instance of the class- and this constructor is always a dunder method __init__, and self we have to pass as an argumnent in the constructor method and self refer to the instance we make of the class. When you make an instance of this class Dog, then this self refer to that object
#self.name is a object propery and the value assigned to it via creating an object and passing the parameter

    def bark(self):
        print(f"{self.name} says woof")  #this bark methood doesnt have any arguments and whenever we create any methood in the class we have to pass the self in it, because any instance of this class can access this object
        

#Lets create some objects

my_dog = Dog("Buddy", "Golden Retriever")
another_dog = Dog("Lucy", "Labrador")

print(my_dog.name, my_dog.breed)
print(another_dog.name, another_dog.breed)
print(my_dog.bark())
print(another_dog.bark())
    
'''
Class Attributes: These are shared by all objects of the class. Like 
species in our Dog class. All dogs belong to the same species. They are
defined outside of any method, directly within the class.
Instance Attributes: These are specific to each individual object. name
and breed are instance attributes. Each dog has its own name and breed.
They are usually defined within the __init__ method.
'''

# #The __init__ method is special. It’s called the constructor. It’s automatically run
# whenever you create a new object from a class.