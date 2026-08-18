
def largest_no(n):
    largest = n[0]
    for i in n:
        if i > largest:
            largest = i
    return largest

#n = [int(x) for x in input("Enter the elements : ").split()]
n = [3, 5, 7, 2, 8]
result = largest_no(n)
print("The largest number is :", result)
