#Print

#It has sep and end parameters
print("Hello", "World")
print("Hello", "World", sep= "-")
print("Hello", "World", sep= "-", end= " ! ")
print("Hello", "World")

#help #It is used to get the documentation of a function or module

help(len)

#range #It is used to generate a sequence of numbers

rng = range(5)
print(rng) #range returns a range object, which is an iterable means you can iterate or loop through it
print(type(rng))  # Check the type of rng
print(list(rng))  # Convert range to list for better visualization

#Map and apply #These are used to apply a function to a sequence of elements
#Apply is used with pandas DataFrame or Series, while map is used with iterables like lists.
# Map is a built-in function that applies a given function to all items in an iterable (like a list or tuple) and returns a map object (which is an iterator).

strings = ["apple", "banana", "cherry", "my", "world"]

print(list(map(lambda x: len(x), strings)))
print([len(x) for x in strings])  # List comprehension equivalent

#Filter #It is used to filter elements from an iterable based on a condition

print(list(filter(lambda x: len(x) > 3, strings)))
print([x for x in strings if len(x) > 3])  # List comprehension


#sum function #It is used to sum up the elements of an iterable
numbers = [1, 2, 3, 4, 5]
print(sum(numbers))
print(sum(numbers, 10))  # Starting value of 10

#sorted function #It is used to sort the elements of an iterable

numbers = [5, 2, 9, 1, 5, 6, -2, -3, 100]

sorted_numbers = sorted(numbers)
print(sorted_numbers)
sorted_numbers_desc = sorted(numbers, reverse=True)
print(sorted_numbers_desc)

#There is one more paramter you can pass to sorted function, which is key. It is used to sort the elements based on a key function.

people = [
    {'name': 'Alice', 'age': 30},
    {'name': 'Bob', 'age': 25},
    {'name': 'Charlie', 'age': 35},
    { 'name': 'David', 'age': 20 }
]

sorted_people = sorted(people, key = lambda x: x['age']) #Here we are sorting the list of dictionaries based on the age key, so key is where we define the function to sort the elements based on a specific key.
print(sorted_people)

#Zip function #It is used to combine two or more iterables (like lists or tuples) into a single iterable of tuples, where each tuple contains elements from the input iterables at the same index.
names = ['Alice', 'Bob', 'Charlie', 'David']
age = [30, 25, 35, 20]

for index in range(len(age)):
    print(f"name: {names[index]}, age: {age[index]}")
    
zip_object = zip(names, age)  # This will return a zip object, which is an iterator
print(zip_object)  # Print the zip object
print(list(zip_object))  # Convert zip object to list for better visualization
print(type(zip_object))  # Check the type of zip_object
print(dict(zip(names, age)))  # Convert zip object to dictionary for better visualization


for name, age in list(zip(names, age)):
    print(f"name: {name}\: age: {age}")