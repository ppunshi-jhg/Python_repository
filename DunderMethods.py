#Dunder methods are special methods that starts and ends with double underscores. They are also known as magic methods. They allow us to define the behaviour of our objects in Python. They are used to implement the behavior of built-in functions and operators. They are mainly used in classes to define how objects of that class behave with respect to built-in operations. As you know Python is an object-oriented programming language, dunder methods are used to define the behavior of objects in Python.Like list is an object in python, so when we call any of the string method like len, append etc, it is actually calling the dunder method of that object. So, in our class we can define the dunder methods to make our class behave like a built-in object. For example, if we want to make our class behave like a list, we can define the dunder methods like __len__, __getitem__, __setitem__, __delitem__, __iter__, etc. These methods will allow us to use the built-in functions and operators on our class objects.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __str__(self):
        return f"Person(name = {self.name}, age = {self.age})"
    
    def __len__(self):
        return self.age
    
    def __mul__(self, other):
        return self.name * other
    
p = Person("Prince", 29)
print(p) #This will call our defined __str__method, and if we didnt define the __str__ method, it will call the default __str__ method of the object class which will return the memory address of the object.
print(len(p)) #This will call our defined __len__ method, and if we didnt define the __len__ method, it will call the default __len__ method of the object class which will return the number of attributes in the object.
print(p.name) #This will access the name attribute of the object.

print(p*2) #This will call our defined __mul__ method, and if we didnt define the __mul__ method, it will raise an error because the * operator is not defined for the object class.