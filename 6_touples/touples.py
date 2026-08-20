#Tuples are another kind of sequence in Python, similar to lists. However, unlike lists, tuples are immutable, meaning that once they are created, their elements cannot be changed, added, or removed. Tuples are defined by enclosing the elements in parentheses ().

x = ('mukul', 'sachin', 'rahul', 'aman')
print(x[0]) # Output: mukul

y = (1, 2, 3, 4, 5)

print(y[1:4]) # Output: (2, 3, 4)
print(max(y)) # Output: 5

for item in x:
    print(item) # Output: mukul sachin rahul aman

for i in y:
    print(i) # Output: 1 2 3 4 5

#immutable
y[3] = 10 # This will raise a TypeError because tuples are immutable and cannot be modified after creation.

j = "ABCD"
j[2] = "Z" # This will also raise a TypeError because strings are immutable in Python.

#THINGS no to do with tuples
x = (1, 2, 3, 4, 5)
x.sort() # This will raise an AttributeError because tuples do not have a sort() method.
x.append(6) # This will raise an AttributeError because tuples do not have an append() method.
x.reverse() # This will raise an AttributeError because tuples do not have a reverse() method.

t = ()
dir(t) # Output: ['count', 'index']

# why touples are used?
# 1. Tuples are faster than lists because they are immutable and have a smaller memory footprint. This makes them more efficient for certain operations, especially when dealing with large datasets.
# 2. Tuples can be used as keys in dictionaries because they are hashable, while lists cannot be used as keys because they are mutable. This allows for more efficient lookups and data retrieval in certain scenarios.


#we can also put a tuble on the left side of an assignment statement, and the values on the right side will be unpacked into the variables on the left side. This is called tuple unpacking.
a, b, c = (1, 2, 3)
print(a) # Output: 1

(x, y) = (4, 'five')
print(y) # Output: five

#Tuples are compareable
(1, 2, 3) < (1, 2, 4) # Output: True
(1, 2, 3) == (1, 2, 3) # Output: True
(1, 2, 3) > (1, 2, 2) # Output: True
