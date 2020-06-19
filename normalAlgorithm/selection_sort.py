def findSmallerOne(_list):
    _smallest = _list[0]
    _smallest_index = 0
    for i in range(1, len(_list)):
        if _list[i] < _smallest:
            _smallest = _list[i]
            _smallest_index = i
    return _smallest_index

def selectionSort(_list):
    _newArr = []
    for i in range(len(_list)):
        _smaller = findSmallerOne(_list)
        _newArr.append(_list.pop(_smaller))
    return _newArr

# 选择排序 O(n*n)

print(selectionSort([5, 4, 2, 8, 9]))