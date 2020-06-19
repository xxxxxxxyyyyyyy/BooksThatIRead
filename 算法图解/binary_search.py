def binary_search(_list, item):
    low = 0
    high = len(_list) - 1
    while low <= high:
        mid = (int)((low + high) / 2)
        temp = _list[mid]
        if temp == item:
            return mid
        if temp > item:
            high = mid - 1
        else:
            low = mid + 1
    return None


#  大O为 O(logn)
my_list = [1, 3, 5, 7, 9]

print(binary_search(my_list, 3))
print(binary_search(my_list, -1))