from Stack import Stack


def next_greater(arr: list) -> list:
    n = len(arr)
    ans = [i * 0 for i in range(n)]
    s = Stack()

    for i in range(1, len(arr) + 1):
        while not s.is_empty() and s.peek() <= arr[-1 * i]:
            s.pop()
        if s.is_empty():
            ans[-1 * i] = i + 1
        else:
            ans[-1 * i] = s.peek()
        s.push(arr[-1 * i])
    return ans


if __name__ == '__main__':
    num = [6, 8, 0, 1, 3]
    print(next_greater(num))
