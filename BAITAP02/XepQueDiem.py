q = int(input())
result = []
for i in range(q):
    n = int(input())
    if (n == 2):
        result.append(2)
    elif (n % 2 == 0):
        result.append(0)
    else:
        result.append(1)
for r in result:
    print(r)
