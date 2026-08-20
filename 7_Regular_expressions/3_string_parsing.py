data = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'

# 1. Find the position of the '@' symbol
atpos = data.find('@')
print(atpos)  # Output: 21

# 2. Find the position of the first space after the '@' symbol
sppos = data.find(' ', atpos)
print(sppos)  # Output: 31

# 3. Slice the string from one character after '@' up to (but not including) the space
host = data[atpos + 1 : sppos]
print(host)  # Output: uct.ac.za