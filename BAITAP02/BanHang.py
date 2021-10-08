q = int(input())
result = []
for i in range(q):
    sum_price = 0
    n = int(input())
    _input = input().split()
    for j in range(n):
        sum_price += int(_input[j])
    if (sum_price % n == 0):
        result.append(int(sum_price / n))
    else:
        result.append(int(sum_price / n) + 1)
for r in result:
    print(r)
