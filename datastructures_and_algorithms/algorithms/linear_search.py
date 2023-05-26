my_list = [1, 5, 12, 47, 65, 80, 22, 34]


def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1  # if target not found


print(linear_search(my_list, 100))
