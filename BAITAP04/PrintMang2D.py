_input = input().split()
r = int(_input[0])
c = int(_input[1])
arr = []
for i in range(r):
    _input = input().split()
    for ii in range(len(_input)):
        _input[ii] = str(int(_input[ii]))
    arr.append(_input)

for i in range(c):
    max_len = 0
    for ii in range(r):
        if (len(arr[ii][i]) > max_len):
            max_len = len(arr[ii][i])
    for ii in range(r):
        arr[ii][i] = ' ' * (max_len - len(arr[ii][i])) + arr[ii][i]

for i in range(r):
    for ii in range(c-1):
        print(arr[i][ii], end=' ')
    print(arr[i][c-1])
