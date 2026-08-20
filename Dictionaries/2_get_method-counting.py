# using get() method to retrieve the value of a key in a dictionary
#inside the get() method, we can provide a default value to return if the key is not found in the dictionary. This is useful to avoid KeyError exceptions when trying to access keys that may not exist.
counts = dict()
names = ['csev', 'cwen', 'csev']
for name in names:
    #if name not in counts:
    #    counts[name] = 1
    #else:
    #    counts[name] = counts[name] + 1
    counts[name] = counts.get(name, 0) + 1
print(counts)  # Output: {'csev': 2, 'cwen': 1}