_input = input().split()
k = int(_input[0])
t = int(_input[1])
period = int(t / k)
if (period % 2 == 0):
    result = t % k
else:
    result = k - (t % k)
print(result)
