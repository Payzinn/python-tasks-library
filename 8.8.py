def binary_search(arr, x, start, end):
    if start > end:
        return -1
    
    mid = (start + end) // 2
    if arr[mid] == x:
        return mid
    
    elif arr[mid] < x:
        return binary_search(arr, x, mid + 1, end)
    
    else:
        return binary_search(arr, x, start, mid - 1)
    
arr = [2, 6, 7, 40, 12, 30, 10, 65]
arr.sort()
x = 12
result = binary_search(arr, x, 0, len(arr)-1)
if result != -1:
    print('Элемент найден в индексе: {}'.format(result))
else:
    print('Элемент не найден')

