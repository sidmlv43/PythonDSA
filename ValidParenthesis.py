from queue import LifoQueue


def is_valid(char_seq):
    s = LifoQueue()
    for i in range(len(char_seq)):
        if char_seq[i] == '[':
            s.put(']')
        elif char_seq[i] == '(':
            s.put(')')
        elif char_seq[i] == '{':
            s.put('}')
        elif s.empty() or s.get() is not char_seq[i]:
            return False

    return s.qsize() == 0


def is_duplicate(char_seq):
    s = LifoQueue()
    for i in range(len(char_seq)):
        ch = char_seq[i]
        if ch == ')':
            count = 0
            while s.get() != '(':
                count += 1
            if count < 1:
                return True
            else:
                s.get()
        else:
            s.put(ch)

    return False


if __name__ == '__main__':
    print(is_valid("{()[]}"))
    print(is_duplicate("(1 + 2 - ((4 * 4))"))