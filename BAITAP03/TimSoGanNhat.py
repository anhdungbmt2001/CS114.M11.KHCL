n = int(input())
a = input().split()
for i in range(n):
    a[i] = int(a[i])
x = input().split()
k = int(x[0])
x = int(x[1])

def sort_key(e):
    return abs(e - x)
a.sort(key=sort_key)
a = a[:k]
a.sort()
for e in a:
    print(e, end=' ')
