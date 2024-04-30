# strings and lists
#strings are immutable- they can't be changed.

name="Prince"
print(name[0:3]) #It gives you 0,1,2 index

# Use input in methond- its an inbuilt function to grab the value from the user but it stores the value in string

age= input("Enter your age") #it returns the value in string- so you need to convert in integer

# print(f"Your age is {int(age)}")


# Some built-in function for strings

print(max(10,20,30))
# min, abs, len, capitalize etc etc

# Lists are mutable-so you can modify it and its like an array

list1= [1,2,3,"Prince"]

print(list1[2])
print(list1[0:2])
print(list1[-1])
list1[2]="Punshi"

print(list1)

# We have modified the value of index 2 in the list 1, so it can be changed and modified

