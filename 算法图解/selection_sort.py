def findSmallerOne(_list):
    smallest = _list[0]
    smallest_index = 0
    for i in range(1, len(_list)):
        if _list[i] < smallest:
            smallest = _list[i]
            smallest_index = i
    return smallest_index

def selectionSort(_list):
    newArr = []
    for i in range(len(_list)):
        _smaller = findSmallerOne(_list)
        newArr.append(_list.pop(_smaller))
    return newArr

# 选择排序 O(n*n)

print(selectionSort([5, 4, 2, 8, 9]))