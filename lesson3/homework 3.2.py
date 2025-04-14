list_of_lists = [
    [12, 3, 4, 10],
    [1],
    [],
    [12, 3, 4, 10, 8]
]
for my_list in list_of_lists:
    if len(my_list) > 1:
        last_element = my_list[-1]
        new_list = [last_element] + my_list[:-1]
    else:
        new_list = my_list
    print(new_list)