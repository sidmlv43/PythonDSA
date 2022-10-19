from sorting import merge_sort, quick_sort

def linear_search(arr, key):
    """

    :param arr:
    :param key:
    :return: index of key in list
    """
    for i in range(len(arr)):
        if arr[i] == key:
            return i

    return -1


def binary_search(arr, key):
    start = 0
    end = len(arr) - 1
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == key:
            return mid
        if arr[mid] < key:
            start = mid + 1
        else:
            end = mid - 1

    return -1


def reverse(arr):
    n = len(arr) - 1
    for i in range(n // 2):
        arr[i], arr[n - i] = arr[n - i], arr[i]


def find_sub_arrays(arr):
    for i in range(len(arr)):
        start = i
        for j in range(i, len(arr)):
            end = j + 1
            for k in range(start, end):
                print(arr[k], end=", ")
            print("\n")


def kadane(arr):
    curr_sum = 0
    max_sum = arr[0]
    for i in range(len(arr)):
        curr_sum += arr[i]
        if curr_sum > max_sum:
            max_sum = curr_sum
        if curr_sum < 0:
            curr_sum = 0

    return max_sum


if __name__ == '__main__':
    lst = [1, 5, 3, 5, 6, 13, 10]
    quick_sort(lst, 0, len(lst)-1)
    print(lst)
    print(binary_search(lst, 3))

    reverse(lst)
    print(lst)
    print(end='\n\n\n')

    find_sub_arrays(lst)