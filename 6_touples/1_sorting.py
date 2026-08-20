d = {'a' : 1, 'b': 2, 'c': 3}
print(d.items())

print(sorted(d.items())) # Output: [('a', 1), ('b', 2), ('c', 3)]

for k, v in sorted(d.items()):
    print(k, v) # Output: a 1 b 2 c 3

#sort by vaues instead of keys
c = {'a' : 10, 'b': 1, 'c': 22}
tmp = [] # or list()
for k, v in c.items():
    tmp.append((v, k)) # create a list of tuples with value as the first element and key as the second element
print(tmp) # Output: [(10, 'a'), (1, 'b'), (22, 'c')]
tmp = sorted(tmp, reverse=True)
print(tmp) #[(22, 'c'), (10, 'a'), (1, 'b')]

#Even shorter version

c = {'a' : 10, 'b': 1, 'c': 22}
print(sorted([(v, k) for k, v in c.items()], reverse=True))
