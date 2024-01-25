# Jan 25
# Tuples are also the iterables in Python (like list, string and set)
# Tuples are immutable datatypes
# Tuple elements are enclosed inside small brackets

# Creating Tuples
a = () # Empty Tuple
b = () # Empty tuple

list(), set(), tuple(), dict(), float(), bool(), str() #these are built-in functions for datatypes

c= (1,2,3) # Non-empty tuple

# Elements can ne of mixed datatypes
d = (1,2.1, "hello", [1,2])

# Accessing tuple elements
# Tuple elements can also be accessed using Indexing and Slicing similar to list

vowels = ("a", "e", "i", "o", "u")
print(vowels[0]) #a
print(vowels[-1]) #u

print(vowels[:2]) # ("a", "e")
print(vowels[3:])  # ("o", "u")
print(vowels[4:2])  # ()
