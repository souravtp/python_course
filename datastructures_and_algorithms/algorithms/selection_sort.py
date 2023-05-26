def selection_sort(arr):
    n = len(arr)  # here 5
    # Traverse through all array elements
    for i in range(n):
        # Find the minimum element in the unsorted sublist
        min_id = i

        for j in range(i+1, n):  # taking all elements except first.
            if arr[j] < arr[min_id]:  # comparing all elements with first element( here 5)
                min_id = j  # index of smallest number is given to min_id
        # Swap the found minimum element with the first element.

        arr[i], arr[min_id] = arr[min_id], arr[i]

    return arr


my_list = [5, 4, 1, 7, 2, 3]  # after first iteration  the list will be [1, 4, 5, 7, 2, 3]
                                # after second iteration list is [1, 2, 5, 7, 4, 3]
print(selection_sort(my_list))