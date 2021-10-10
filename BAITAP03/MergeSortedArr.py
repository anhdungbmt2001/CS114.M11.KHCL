n_input = input().split()
n_a = int(n_input[0])
n_b = int(n_input[1])
a = []
b = []
_input = input().split()
for i_ in _input:
    a.append(int(i_))
_input = input().split()
for i_ in _input:
    b.append(int(i_))
result = []
ia = ib = 0
while (ia < n_a and ib < n_b):
    if a[ia] <= b[ib]:
        result.append(a[ia])
        ia += 1
    else:
        result.append(b[ib])
        ib += 1
if (n_a <= n_b):
    while (ib < n_b):
        result.append(b[ib])
        ib += 1
elif (n_a > n_b):
    while (ia < n_a):
        result.append(a[ia])
        ia += 1
for r in result:
    print(r, end=' ')
