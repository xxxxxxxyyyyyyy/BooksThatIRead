def binary_search(_list, item):
    _low = 0
    _high = len(_list) - 1
    while _low <= _high:
        mid = (int)((_low + _high) / 2)
        temp = _list[mid]
        if temp == item:
            return mid
        if temp > item:
            _high = mid - 1
        else:
            _low = mid + 1
    return None


#  大O为 O(logn)
my_list = [1, 3, 5, 7, 9]

print(binary_search(my_list, 3))
print(binary_search(my_list, -1))