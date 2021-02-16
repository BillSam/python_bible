def fib(number):
    a = 0
    b = 1
    for i in range(number):
        yield a
        temp = a
        a = b
        b = temp + b


fib_list = [x for x in fib(20)]
print(fib_list)
