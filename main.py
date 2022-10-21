from SinglyLinkedList import LinkedList
from DoublyLinkedList import DoublyLinkedList
from sorting import quick_sort

if __name__ == "__main__":
    nums = [4, 0, 2, 1, 18, 7, 9, 12, 11, 10, 8, 5]
    quick_sort(nums, 0, len(nums) - 1)
    print(nums)
