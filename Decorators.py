# Decorators - Its main purpose is to modify th behavior of a function or method. Just add some extra functionality to an existing function without modifying its structure.
# func is a function that takes a string as a parameter and inside that fucntion there is a wrapper function that prints "Started", the string passed to func, and "Ended". But the main func does not execute the wrapper function, it just returns the wrapper function. So to call the wrapper function, we need to call func with a string and then call the returned wrapper function.

# def func(string):
#     def wrapper():
#         print(f"Started")
#         print(f"{string}")
#         print(f"Ended")
        
#     return wrapper

# func("Hello") #here we are calling func with "Hello" but not calling the wrapper function, so it won't print anything yet.
# #To call the wrapper function we have two choices : either we can assign the returned wrapper function to a variable and then call that variable, or we can call the wrapper function directly by calling func("Hello")().

# #First way:

# func("Hello")()  # This will print "Started", "Hello", and "Ended".

# func_wrapper = func("Hello")  # This assigns the wrapper function to a variable.
# func_wrapper()  # This will also print "Started", "Hello", and "Ended".


#2ND EXAMPLE
#Now lets take an example if intead of passign the string to the function, we pass a function to the func
#Here we will create a decorator that takes a function as an argument and wraps it with additional functionality. The decorator will print "Started" before calling the function and "Ended" after calling it.
# def func(func_to_call):
#     def wrapper():
#         print(f"Started")
#         func_to_call()
#         print(f"Ended")
        
#     return wrapper

# def function_to_call():
#     print("This is the function to call.")
    
# func(function_to_call)  #Here we are calling func with function_to_call, but not calling the wrapper function, so it won't print anything yet.

# func(function_to_call)()  # This will print "Started", "This is the function to call.", and "Ended".

#Before we check out the third example , first there is a better way to use decorators in Python. Instead of manually calling the wrapper function, we can use the `@decorator_name` syntax to apply the decorator to a function. This is a more Pythonic way to use decorators.

# def func(func_to_call):
#     def wrapper():
#         print(f"Started")
#         func_to_call()
#         print(f"Ended")
        
#     return wrapper

# @func  # This applies the decorator to the function below. What it does is the below function to call is passed to the func decorator, which returns the wrapper function. 
# def function_to_call():
#     print("This is the function to call.")

# # Now, when we call function_to_call, it will automatically be wrapped by the decorator.
# function_to_call()  # This will print "Started", "This is the function to call", and "Ended".

#3RD EXAMPLE

#Now lets take an example where the function we're passing to the decorator takes an argument 

# def func(func_to_call):
#     def wrapper(x):
#         print(f"Started")
#         func_to_call(x)
#         print(f"Ended")
    
#     return wrapper

# @func  # This applies the decorator to the function below.
# def function_to_call(x):
#     print(f"This is the function to call with argument: {x}")


# function_to_call(5)  # This will print "Started", "This is the function to call with argument: 5", and "Ended".

# whys that?
# Please see the explanation: Let me break this down step by step in simple terms:

# 1. What is a decorator?
# A decorator is a way to modify or enhance the behavior of a function without changing its actual code. In Python, you use the @decorator_name syntax to apply a decorator to a function.

# 2. What does func do?
# The func function is a decorator. It takes another function (func_to_call) as input and wraps it inside another function called wrapper. The wrapper function adds extra behavior (printing "Started" and "Ended") before and after calling the original function (func_to_call).

# 3. How does the @func decorator work?
# When you write @func above a function, Python automatically passes that function (function_to_call) to the func decorator. The func decorator then returns the wrapper function, which replaces the original function.

# So, after applying the decorator, calling function_to_call(5) is actually calling the wrapper function returned by func.

# 4. Why does function_to_call(5) work?
# When you call function_to_call(5), Python is not directly calling the original function_to_call. Instead, it is calling the wrapper function returned by the decorator.
# The wrapper function takes the same arguments as the original function (x in this case) and calls the original function (func_to_call(x)) inside it.


# 4th Exmaple
#Case where we have one decorator and we call that decorator on two function one with no argument and one with an argument, so we use *args and **kwargs to handle both cases.

# def func(func_to_call):
#     def wrapper(*args, **kwargs):
#         print(f"Started")
#         print(f"Arguments: {args}, Keyword Arguments: {kwargs}")
#         print(f"Ended")
        
#     return wrapper


# @func
# def function_to_call_no_args():
#     print("This is the function with no arguments.")
    
# @func
# def function_to_call_with_args(x):
#     print(f"This is the function to call with argument: {x}")
    
# function_to_call_no_args()  # This will print "Started", "Arguments: (), Keyword Arguments: {}", and "Ended".
# function_to_call_with_args(5)  # This will print "Started", "Arguments: