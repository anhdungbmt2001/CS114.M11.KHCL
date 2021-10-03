def Fibonacci(n):
    if n < 0:
        return
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return Fibonacci(n-1) + Fibonacci(n-2)

x = int(input())
if (x >= 1 and x <= 30):
    print(Fibonacci(x))
else:
    print("So", x, "khong nam trong khoang [1,30].")
