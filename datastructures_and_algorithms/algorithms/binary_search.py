def binary_search(arr, target):
    left, right = 0, len(arr) - 1  # defining range of index positions to search.
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:  # if the middle value is less than the search value, search value will be in right side
            left = mid + 1        # of the middle. So, we set left as next index of current middle.
        else:
            right = mid - 1
    return -1  # if target not found


my_list = [5, 14, 28, 96, 42, 32, 78, 55, 64, 46, 83]  # data should be sorted
my_list.sort()
print(my_list)
print(binary_search(my_list, 42))
print(binary_search(my_list, 46))
print(binary_search(my_list, 99))
