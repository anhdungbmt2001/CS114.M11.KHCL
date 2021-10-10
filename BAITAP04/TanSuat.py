q = int(input())
_result = []
for i in range(q):
    _input = input().split()
    n = int(_input[0])
    k = _input[1]
    _input = input().split()
    _result.append(_input.count(k))
for e in _result:
    print(e)
