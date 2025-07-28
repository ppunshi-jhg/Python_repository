#Eval - is used to evaluate the code which is written in the string format

source: str = "10+20+30"
result: int = eval(source)
print(result)
print(type(result))

source2: str = "str(10+20*2) + 'hello'"
print(eval(source2))
print(type(eval(source2)))


user_input: str = input("Enter a expression to evaluate: ")
print(eval(user_input))

#Exec- is more powerful tha eval, it executes the multiple lines of code

source3: str = """
print(f"Hello World!")
def add(a,b):
    return a+b
    
print(add(10,20))
"""

exec(source3)