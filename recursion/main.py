def find_sum(n):
    if n == 1:
        return n
    return n + find_sum(n - 1)


def fib(n):
    if n == 0 or n == 1:
        return n

    return fib(n - 1) + fib(n - 2)


if __name__ == "__main__":
    print(fib(2))
