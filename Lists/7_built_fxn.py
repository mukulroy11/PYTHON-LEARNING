nums = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
print(len(nums)) # Output: 11
print(max(nums)) # Output: 9
print(min(nums)) # Output: 1
print(sum(nums)) # Output: 44
print(sum(nums)/len(nums)) # Output: 4.0

numlist = []
while True:
    inp = input('Enter a number: ')
    if inp == 'done':
        break
    value = float(inp)
    numlist.append(value)
print(numlist)
avg = sum(numlist)/len(numlist)
print('Average:', avg)