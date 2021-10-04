# https://khmt.uit.edu.vn/wecode/cs114x/assignment/2/1

def PhatDeBai(n, k, p, q):

    if (q == 1):
        Alice_i = p * 2 - 2
    else:
        Alice_i = p * 2 - 1
    Bob_i = [Alice_i + k, Alice_i - k]
    if (Bob_i[0] >= n and Bob_i[1] < 0):
        return -1
    u = [0, 0]
    v = [0, 0]
    j = 0
    for i in Bob_i:
        if (i % 2 == 0):
            u[j] = int(i / 2) + 1
            v[j] = 1
        else:
            u[j] = int((i + 1) / 2)
            v[j] = 2
        j += 1

    if (p - u[1] <= u[0] - p and u[1] > 0):     ###
        return [u[1], v[1]]
    else:
        return [u[0], v[0]]

# Test 25: return [u[1], v[1]]

n = int(input())
k = int(input())
p = int(input())
q = int(input())

result = PhatDeBai(n, k, p, q)
if (result == -1):
    print(result)
else:
    print(result[0], result[1])
