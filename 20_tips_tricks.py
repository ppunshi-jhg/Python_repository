# 1. Swapping Variables
# a,b = 5,10
# print(f"Before Swap: a = {a}, b = {b}")

# a,b = b,a

# print(f"After Swap: a ={a}, b = {b}")

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


# 2. Reversing Iterables

# names = ["Alice", "Bob", "Charlie"]

# print("Original List:", names)

# print(f"names after revering {names[::-1]}")

# #What if I want the names not in string but just with a comma

# print(", ".join(names[::-1]))
# print(*names[::-1])
# print(names)

# #To reverse a string you can use the slicing method as it doesnt change the original string, but if you want to change the original string you can use the reversed function

# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 3. One line conditions

# number: int = 10

# print(True if number > 10 else False)

# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# # 4. Getting values from a dictionary
# info: dict[str, str] = { 'name' : 'Alice', 'age': '30', 'city': 'New York' }

# print(info.get("Prince"))
# print(info.get("Prince", "Not found"))


# 5. Getting and Setting Values

# scores: dict[str, int]= {'Alice': 90, 'Bob': 85, 'charlie': 92}

# print(f"Scores before update: {scores}")

# prince_score: int = scores.setdefault('Prince', 75)

# print(f"scores after update:  {scores}")

# setdefault guarantees the key is present after it runs (with the provided value if it was missing).

#Using counters in python

from collections import Counter
#Counter is a subclass of dict that helps count hashable objects. It is useful for counting occurrences of items in an iterable. it acts like a dictionary where keys are the items and values are their counts.
letters: list[str] = ['a', 'b', 'c', 'a', 'b', 'a']
letter_count: Counter = Counter(letters)
print(f"Letter counts: {letter_count}")
print(f"Total: {letter_count.total()}")
print(f"Most common letter: {letter_count.most_common(1)}")


#Enumerate help you to iterate over an iterable

str_letters: str = "hello"

for index, element in enumerate(str_letters):
    print(f"{index} : {element}")
    #if you wnat to start the index from 1 you can use the start parameter
for index, element in enumerate(str_letters, start=1):
    print(f"{index} : {element}")
    
#Merging Dictionaries: You can do with several ways in python 3.9 and above, with the | operator, unpacking, or the update method.

a: dict[str, int] = {'a': 1, 'b': 2}
b: dict[str, int] = {'c': 3, 'd': 4}

print(a|b) #Merging using the | operator
a |= b #It merges b into a
print(a)
print({**a, **b}) #Merging using unpacking

#Callable classes: A callable class is a class that implements the __call__ method, allowing instances of the class to be called like functions. So, when ypou make an instance of this class which has call dunder method, you can call the instance with parenthesis like a function.

class Multiplier:
    def __init__(self, value: int):
        self.value = value
    def __call__(self, x:int) -> int:
        return self.value * x

triple = Multiplier(3) #Here we create an instance of the Multiplier class with value 3
#If I want to call this instance like a function, I can do it like this
result = triple(5) # This will call the __call__ method with x=5

print(f"{result}")

#or you can do the whole directly like this
print(Multiplier(3)(5))  # This will also output 15, calling the __call__ method directly

#String replacement

sentence: str = 'The tired red fox on the red farm ate a bored red pig.'

print(sentence.replace('red', 'blue')) #Replace all occurrences of 'red' with 'blue' as from the tired and bored as well because it is a string method that replaces all occurrences of the specified substring.

print(sentence.replace(' red', ' blue')) #Replace only the occurrences of 'red' that are preceded by a space, so it will not replace the 'red' in 'tired' and 'bored'.

