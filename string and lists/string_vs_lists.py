a = 'I am Mukul'
b = a.split() # split the string into a list of words
print(b) # Output: ['I', 'am', 'Mukul']
print(len(b)) # Output: 3
print(b[0]) # Output: I

for i in b:
    print(i) # Output: I am Mukul

for i in a:
    print(i) # Output: I a m M u k u l

l = ' i am                mukul'
b = l.split() # split the string into a list of words
print(b) # Output: ['i', 'am', 'mukul']

thing = 'first;second;third'
d = thing.split()
print(d) # Output: ['first;second;third']
print(len(d)) # Output: 1

c = thing.split(';') # split the string into a list of words using ';' as the delimiter
print(c) # Output: ['first', 'second', 'third']