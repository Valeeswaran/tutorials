arr = [1, 2, 3, 4, 4, 4, 5, 6, 6, 7, 8, 9]
arr.sort()
my_dict = {i:arr.count(i) for i in arr}

# sorting the dictionary based on value
my_dict = {k: v for k, v in sorted(my_dict.items(), key=lambda item: item[1])}

print(len(my_dict))
print(my_dict)
list = list(my_dict.keys())
print(list[-1])

