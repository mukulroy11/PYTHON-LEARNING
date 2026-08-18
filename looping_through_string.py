fruit = 'banana'
i = 0
while i < len(fruit):
    letter = fruit[i]
    print(i, letter)
    i = i + 1

# for loop is much more elegant and easier to read than a while loop
for letter in fruit:
    print(letter)