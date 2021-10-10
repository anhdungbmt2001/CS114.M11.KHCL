_input = input().split()
n = int(_input[0])
m = int(_input[1])
_input = input().split()
r = int(_input[0])
c = int(_input[1])

arr = []
for i in range(n):
    _input = input().split()
    for e in _input:
        arr.append(e)

if (n * m == r * c):
    for i in range(len(arr)):
        if ((i+1) % c == 0):
            print(arr[i])
        else:
            print(arr[i], end=' ')
else:
    for i in range(len(arr)):
        if ((i+1) % m == 0):
            print(arr[i])
        else:
            print(arr[i], end=' ')
