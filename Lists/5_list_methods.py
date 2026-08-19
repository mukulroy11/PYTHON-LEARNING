x = list()
print(dir(x)) #['append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']

s = []
s.append('mukul')
s.append('sahil')

s.append('rahul')
s.insert(1, 'rohit') # insert at index 1
print(s) # Output: ['mukul', 'rohit', 'sahil', 'rahul']
s.pop() # remove last element
print(s) # Output: ['mukul', 'rohit', 'sahil']