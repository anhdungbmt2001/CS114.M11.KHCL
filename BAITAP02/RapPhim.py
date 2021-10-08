_input = input().split()
n = int(_input[0])
m = int(_input[1])
a = int(_input[2])

if (m % a == 0):
    num_m = int(m / a)
else:
    num_m = int(m / a) + 1
if (n % a == 0):
    num_n = int(n / a)
else:
    num_n = int(n / a) + 1
print(num_m * num_n)
