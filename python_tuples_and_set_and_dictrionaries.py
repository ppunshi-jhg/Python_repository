# Tuples are immutable like strings 

t=(1,2,3)

print(t[0])
# t[0]=2 this wont work as you cant change the tuple value
print(len(t))

# Sets only cntain unique set of values, even if you define multiple same values it will show you just the unique value when you print it- and set is immutable as well

set1={1,2,3,3,3,4,4,5}
set2={3,23,24,5}

print(set1)

print(set1.union(set2))

a=set()  #Way to create empty set

print(a)

#dictionaries are mutable and it stores the value in key:value pair

marks={"Prince":95,"Dhwani":34,"Dush":30}

print(marks.keys())
print(marks.values())
print(marks["Prince"])

# get is also used to fetch the value from the dictionary, but marks["prince2"] will give yu an error as this key is not present in dictionary, but if we use marks.get("Prince2") it wont give you an error

print(marks.get("Prince2"))