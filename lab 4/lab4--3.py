my_list = [1, 2, 2, 4, 4, 5, 6]
new_list = list(dict.fromkeys(my_list))
print("List after removing duplicates:", new_list)