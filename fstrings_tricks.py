#1st Trick is to capture the long numbers

n: int = 12345678901234567890
print(f"{n:,}")
print(f"The longest numbr can be represented linke this : {n: _}") 

#The above code is for users to see long numbers in a more readable format with commas or spaces.

#And for the developers you can use the following while assigning the value to the variable
n: int = 12_345_6789_0123_4567_890

print(f"This will be represented the complete number: {n}")

n: int = 1.2345678
print(f"{n:.2f}")

#2nd Trick is to use f strings for aliginment the text

name: str = "Alice"

print(f"The name can be represented right aligned like this: {name:>20}")
print(f"The name can be represented left aligned like this: {name:<20}") #But this is by default
print(f"The name can be represented center aligned like this: {name:^20}")
print(f"The name can be represented center aligned like this: {name:~^20}") #It means that the name will be center aligned and the remaining space will be filled with ~ character
print(f"The name is right aligned with the filled character: {name:*>20}")
# print(f"The name is right aligned with the filled character: {name:!>20}") #This one wont work because ! is not a valid fill character, but if you want to use it, you can use it like this
print(f"The name is right aligned with the filled character: {name:!<20}")
print(f"The name is right aligned with the filled character: {name:!>20}") 

#3rd Trick

from datetime import datetime

now: datetime = datetime.now()
print(f"The current date and time is : {now}")
print(f"The current date and time is : {now:%d:%m:%y %H:%M:%S}")  # Custom format for date and time

#4th trick

a: int = 5
b: int = 10

print(f"The sum of a+b is: {a+b}")
print(f"The sum of {a+b = }")