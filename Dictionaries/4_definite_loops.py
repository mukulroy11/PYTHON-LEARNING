counts = {'mukul': 1, 'sachin': 2, 'rahul': 1}
for key in counts:
    print(key, counts[key])

#get a list of keys, values or item(both key and value) from a dictionary

print(counts.keys()) # Output: dict_keys(['mukul', 'sachin', 'rahul'])
print(counts.values()) # Output: dict_values([1, 2, 1])
print(counts.items()) # Output: dict_items([('mukul', 1), ('sachin', 2), ('rahul', 1)])