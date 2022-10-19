from Stack import Stack


def stock_span(stocks: list, spans: list) -> None:
    s = Stack()
    spans[0] = 1
    s.push(0)

    for i in range(1, len(stocks)):
        cur_price = stocks[i]
        while not s.is_empty() and cur_price > stocks[s.peek()]:
            s.pop()
        if s.is_empty():
            spans[i] = i + 1
        else:
            prev_high = s.peek()
            spans[i] = i - prev_high
        s.push(i)


if __name__ == "__main__":
    stock = [100, 80, 60, 70, 60, 85, 100]
    span = [i * 0 for i in range(len(stock))]
    stock_span(stock, span)
    print(span)