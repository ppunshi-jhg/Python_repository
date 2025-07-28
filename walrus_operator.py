#Walrus operator means the value is assigned to a variable and then used in the same expression. It was introduced in Python 3.8. The walrus operator is useful for reducing code duplication and improving readability, especially in loops and conditional statements.

#Without walrus operator

# data: str = input("Enter something: ")  #here assign the value to a variable
# while data != "quit":   #Here we use the variable in the condition, this is an expression
#     print(f"You entered: {data}")
#     data = input("Enter something: ")


#With walrus operator:

while (data := input("Enter something: ")) != "quit":
    print(f"You entered: {data}")  # Here, the walrus operator assigns the input to `data` and checks the condition in one line.
    
    #With walrus operator

if (value := len("example")) > 5:
    print(f"Length is {value}")  # Here, the walrus operator assigns the length to `value` and checks the condition in one line.
    
# Without walrus operator

numbers = [1, 2, 3, 4, 5]
squares = [x**2 for x in numbers if x**2 > 10]

print(squares)

[square for x in numbers if (square := x**2) > 10]