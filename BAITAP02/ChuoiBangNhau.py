def check(s, t):
    for i in range(len(s)):
        for j in range(len(t)):
            if (s[i] == t[j]):
                return "YES"
    return "NO"

q = int(input())
result = []
for i in range(q):
    s = input()
    t = input()
    result.append(check(s, t))
for r in result:
    print(r)
