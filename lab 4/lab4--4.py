my_list = [2, 3, 2, 4, 5, 3, 2]
freq = {}
for item in my_list:
    freq[item] = freq.get(item, 0) + 1
print("Frequency of elements:", freq)