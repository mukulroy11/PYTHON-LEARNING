file = open('E:\PYTHON LEARNING\Reading files\m.txt')
for i in file:
    print(i)

fhand = open('E:\PYTHON LEARNING\Reading files\m.txt')
count = 0
for line in fhand:
    count = count + 1
print('Line Count:', count)

fhand = open('E:\PYTHON LEARNING\Reading files\m.txt')
inp = fhand.read()
print(len(inp))