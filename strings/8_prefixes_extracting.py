l = 'PLease have a nice day'
print(l.startswith('P'))
print(l.startswith('Please'))


#extracting the prefix from a string
data = 'wHERE @IS THE DATA'
print(data.lower())

a = data.find('@')
print(a)

b = data.find(' ', a)
print(b)

print(data[a+1:b])