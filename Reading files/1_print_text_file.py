file = open('E:\PYTHON LEARNING\Reading files\m.txt')
for i in file:
    print(i)

fhand = open('E:\PYTHON LEARNING\Reading files\m.txt')
count = 0
for line in fhand:
    count = count + 1
print('Line Count:', count)

fhand = open('E:\PYTHON LEARNING\Reading files\m.txt')
#fhand = open('E:\PYTHON LEARNING\Reading files\m.txt', 'r')
inp = fhand.read()
print(len(inp))

fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip() # rstrip() is used to remove the extra whitespace or newline character from the end of the line
    if line.startswith('From:'):
        print(line)