_input = input().split()
n = int(_input[0])
m = int(_input[1])
temp = len(_input[1]) - len(_input[0])

if (n > m):
    print(0)
elif (temp == 0):
    print(1)
else:
    _result = int(_input[1][:temp])
    if (int(_input[1][temp:]) >= n):
        _result += 1
    print(_result)
