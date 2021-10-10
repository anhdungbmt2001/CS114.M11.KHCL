# https://khmt.uit.edu.vn/wecode/cs114x/assignment/4/48

online_list = []
_result = []
while (1):
    _input = input()
    if (_input == '0'):
        break
    _input = _input.split()
    _input[1] = int(_input[1])
    if (_input[0] == '1'):
        online_list.append(_input[1])
    else:
        _result.append(int(online_list.__contains__(_input[1])))
for e in _result:
    print(e)
