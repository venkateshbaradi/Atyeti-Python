# how to generate fibonacci series in python
def fibonacci_series(n):
    x = 0
    y = 1
    result = []

    for mem in range(n):
        result.append(x)
        x, y = y, x+y

    return result


print(fibonacci_series(10))


