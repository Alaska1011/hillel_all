def absolut(lst):
    if len(lst) <= 1:
        return lst
    last_element = lst[-1]
    return [last_element] + lst[:-1]
print(absolut([12,3,4,10,]))
print(absolut([1]))
print(absolut([]))
print(absolut([12, 3, 4, 10, 8]))`