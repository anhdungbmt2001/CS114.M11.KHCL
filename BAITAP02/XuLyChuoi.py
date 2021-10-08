_input = []
_input[:0] = input().lower()
i = 0
while (i < len(_input)):
    if (_input[i] in ['a', 'o', 'y', 'e', 'u', 'i']):
        _input.pop(i)
    else:
        _input[i] = '.' + _input[i]
        i += 1
for j in range(len(_input)):
    print(_input[j], end='')
