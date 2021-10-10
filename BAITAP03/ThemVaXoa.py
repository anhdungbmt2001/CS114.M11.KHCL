# https://khmt.uit.edu.vn/wecode/cs114x/assignment/4/56

arr = []
while (1):
    _input = input().split()
    if (_input[0] == '0'):
        arr.insert(0, _input[1])
    elif (_input[0] == '1'):
        arr.append(_input[1])
    elif (_input[0] == '2'):
        try:
            arr.insert(arr.index(_input[1]) + 1, _input[2])
        except:
            arr.insert(0, _input[2])
    elif (_input[0] == '3'):
        try:
            arr.remove(_input[1])
        except:
            continue
    elif (_input[0] == '4'):
        while (1):
            try:
                arr.remove(_input[1])
            except:
                break
    elif (_input[0] == '5'):
        try:
            arr.pop(0)
        except:
            continue
    elif (_input[0] == '6'):
        break
for e in arr:
    print(e, end=' ')
