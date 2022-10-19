def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(i, len(arr)):
            if arr[j] < arr[i]:
                arr[j], arr[i] = arr[i], arr[j]


def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i, len(arr)):
            if arr[j] < arr[i]:
                min_idx = j

        arr[i], arr[min_idx] = arr[min_idx], arr[i]


def insertion_sort(arr):
    for i in range(len(arr)):
        curr = arr[i]
        prev = i - 1
        while prev >= 0 and arr[prev] > curr:
            arr[prev + 1] = arr[prev]
            prev -= 1
        arr[prev + 1] = curr


def partition(arr, si, ei):
    pivot = arr[ei]
    i = si - 1
    for j in range(si, ei):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    i += 1
    arr[ei] = arr[i]
    arr[i] = pivot
    return i


def quick_sort(arr, si, ei):
    if si >= ei:
        return
    p_idx = partition(arr, si, ei)
    quick_sort(arr, si, p_idx - 1)
    quick_sort(arr, p_idx + 1, ei)


def merge(arr, si, mid, ei):
        n = (ei - si) + 1
        temp = [i * 0 for i in range(n)]
        i = si
        j = mid + 1
        k = 0

        while i <= mid and j <= ei:
            if arr[i] <= arr[j]:
                temp[k] = arr[i]
                i += 1
            else:
                temp[k] = arr[j]
                j += 1
            k += 1

        while i <= mid:
            temp[k] = arr[i]
            i += 1
            k += 1
        while j <= ei:
            temp[k] = arr[j]
            j += 1
            k += 1

        i = si
        for k in range(0, len(temp)):
            arr[i] = temp[k]
            i += 1


def merge_sort(arr, si, ei):
    if si >= ei:
        return
    mid = si + (ei - si) // 2
    merge_sort(arr, si, mid)
    merge_sort(arr, mid+1, ei)
    merge(arr, si, mid, ei)


if __name__ == '__main__':
    numbers = [3, 2, 1, 4, 0, 7, 12, 5]
    merge_sort(numbers, 0, len(numbers) - 1)
    print(numbers)
    # print(merge([1, 2], 0, 4, 8))
