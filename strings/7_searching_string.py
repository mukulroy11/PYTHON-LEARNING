# find() function to search for a substring within another string, not foun return -1
fruit = 'banana'
pos = fruit.find('na')
print(pos)

a = fruit.find('z')
print(a)

#search and replace

a = fruit.replace('banana', 'apple')
print(a)

b = fruit.lower()
print(b)

c = fruit.upper()
print(c)

g = '   banana   '
print(g.lstrip())
print(g.rstrip())
print(g.strip())