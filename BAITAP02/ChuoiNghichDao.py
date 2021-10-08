_normal_input = input()
_inverse_input = input()
_inverse_inversed = ""
i = len(_inverse_input) - 1
while (i >= 0):
    _inverse_inversed += _inverse_input[i]
    i -= 1
if (_inverse_inversed == _normal_input):
    print("YES")
else:
    print("NO")
