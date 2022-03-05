a_list = [1, 2, 3]

sorted_elements = [a_list[index] <= a_list[index+1] for index in range(len(a_list)-1)]
print(sorted_elements)
OUTPUT
[True, True]

is_sorted = all(sorted_elements)
print(is_sorted)
OUTPUT
True