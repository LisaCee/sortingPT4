def partition(data):
    left, pivot, right = [], data[0], []
    for val in data[1:]:
        if val <= pivot:
            left.append(val)
        else:
            right.append(val)
    return left, right, pivot


def quick_sort(nums):
    if len(nums) <= 1:
        return nums
    left, right, pivot = partition(nums)
    return quick_sort(left) + [pivot] + quick_sort(right)

# TO-DO: complete the helpe function below to merge 2 sorted arrays


def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = []
    # TO-DO
    while len(arrA) > 0 and len(arrB) > 0:
        i = 0
        if arrA[i] > arrB[i]:
            merged_arr.append(arrB[i])
            arrB.remove(arrB[i])
        else:
            merged_arr.append(arrA[i])
            arrA.remove(arrA[i])
    while len(arrA) > 0:
        merged_arr.append(arrA[i])
        arrA.remove(arrA[i])
    while len(arrB) > 0:
        merged_arr.append(arrB[i])
        arrB.remove(arrB[i])
    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    # TO-DO
    if len(arr) <= 1:
        return arr

    arrA, arrB = arr[0: len(arr)//2], arr[len(arr) // 2:]

    arrA = merge_sort(arrA)
    arrB = merge_sort(arrB)

    return merge(arrA, arrB)


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr


def merge_sort_in_place(arr, l, r):
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):

    return arr
