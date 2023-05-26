def bubble_sort(arr):
    n = len(arr)
    # Traverse through all array elements
    for i in range(n):
        # Last i elements are already sorted
        for j in range(0, n-i-1):
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


my_list = [5, 1, 40, 27, 54, 15, 3, 98, 63, 33]
# [1, 5, 40, ....] compared 1,5 and swapped
# [1, 5, 40, 27, ....] compared 5 and 40 and swap did not happen
# [1, 5, 27, 40, ....] compared 40 and 27 and swapped


print(bubble_sort(my_list))
