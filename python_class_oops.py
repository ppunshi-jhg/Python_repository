# Let's say a person A has sales of 5000 RS and profit of 2000 Rs and a person spend 1000 Rs on ads, so how you store these things- in a variable right. Now- lets say there is another person B having sales, profit and ads so you cant store value into the same variables so you need to create different varibale for person B , and same for person C stc stc. So- whats the best approach?

# Create a class, and let everyone use that class variable and methods. Class is a blueprint and we use that blueprint and it shows how the objects will look alike. When you make an object of that class- you get acces to their varibales and methods. 

class Person:
    name="Prince"
    occupation="System Engineer"
    
a= Person()
print(a.name)

# You can change a name of the Person class as well with the instance a, as we have assign a value to name variable in class Person, whoich is not the right practice but you will come to know soon whats the best practice

a.name="Dhwani"
print(a.name)