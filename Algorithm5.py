#Implement the selection sort algorithm that is sorting in descending order

# def selection_sort(arr):
#     arr = [9, 7, 4, 1, 3]
#     for i in range(len(arr)):
#         min_value = i
#         for j in range(i + 1, len(arr)):
#             if arr[j] > arr[min_value]:
#                 min_value = j
#             arr[i], arr[min_value] = arr[min_value], arr[i]
#
#             print(arr)
#
# list_to_sort = [9, 7, 4, 1, 3]
# print(list_to_sort)
# selection_sort(list_to_sort)

# Bubble Sort
# Implement the bubble sort algorithm that is sorting in descending order.

# def bubble_sort(arr):
#     for i in range(len(arr)):
#         for j in range(len(arr) - i - 1):
#             if arr[j] > arr[j + 1]:
#                 arr[j], arr[j + 1] = arr[j + 1], arr[j]
#
#                 print(arr)
# list_to_sort = [6, 3, 2, 4, 7, 5]
# print(list_to_sort)
# bubble_sort(list_to_sort)

# Insertion Sort
# Implement the insertion sort algorithm that is sorting in descending order

# def insertion_sort(arr):
#     for i in range(1, len(arr)):
#         key = arr[i]
#         j = i - 1
#
#         while j >= 0 and key < arr[j]:
#             arr[j + 1] = arr[j]
#             j -= 1
#         arr[j + 1] = key
#
#     print(arr)
#
# list_to_sort = [9, 10, 3, 4, 1]
# print(list_to_sort)
# insertion_sort(list_to_sort)

# Merge sort
# Implement the merge sort algorithm that is sorting in descending order.

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    middle = len(arr) // 2
    return merge_arrays(merge_sort(arr[:middle]), merge_sort(arr[middle:]))
def merge_arrays(left_arr, right_arr):
    merged_arrays = []
    i = j = 0
    while i < len(left_arr) or j < len(right_arr):
        if i == len(left_arr):
            merged_arrays.append(right_arr[j])
            j += 1
            continue
        if j == len(right_arr):
            merged_arrays.append(left_arr[i])
            i += 1
            continue

        if left_arr[i] <= right_arr[j]:
            merged_arrays.append(left_arr[i])
            i += 1
        else:
            merged_arrays.append(right_arr[j])
            j += 1

    return merged_arrays

#print(merge_arrays([3, 7], [1, 8]))
list_to_sort = [6, 9, 2, 5, 3, 1]
print(list_to_sort)
print(merge_sort(list_to_sort))










