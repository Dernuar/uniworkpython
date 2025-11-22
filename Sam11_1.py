def fib(n):
    a, b = 1, 1
    count = 0
    while count < n:
        yield a
        a, b = b, a + b
        count += 1

if __name__ == '__main__':
    fibo = fib(200)
    for i in fibo:
        result = i
    print(result)