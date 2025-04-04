def absolut2(lst):
    if not lst:
        return [[], []]

    mid_index = (len(lst) + 1) // 2
    first_list = []
    second_list = []

    for i in range(len(lst)):
        if i < mid_index:
            first_list.append(lst[i])
        else:
            second_list.append(lst[i])

        return [first_list, second_list]
print(absolut2([1, 2, 3, 4, 5, 6]))
print(absolut2([1,2,3]))
print(absolut2([1,2,3,4,5]))
print(absolut2([1]))
print(absolut2([0]))