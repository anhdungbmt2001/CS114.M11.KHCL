def check_vocab(s):
    if (s.endswith('lios')):
        return [1, 1]
    elif (s.endswith('liala')):
        return [1, 2]
    elif (s.endswith('etr')):
        return [2, 1]
    elif (s.endswith('etra')):
        return [2, 2]
    elif (s.endswith('initis')):
        return [3, 1]
    elif (s.endswith('inites')):
        return [3, 2]
    else:
        return 0

def check_Lans_lang(s):

    if (len(s.split()) == 1):
        if (check_vocab(s) != 0):
            return "YES"
        return "NO"

    s = s.split()
    count_noun = 0
    for i in range(len(s)):
        s[i] = check_vocab(s[i])
        if (s[i] == 0):
            return "NO"
        if (s[i][0] == 2):
            count_noun += 1
            if (count_noun > 1):
                return "NO"
    if (count_noun == 0):
        return "NO"

    gender = s[0][1]
    for w in s:
        if (w[1] != gender):
            return "NO"
    
    for i in range(len(s) - 1):
        if (s[i+1][0] - s[i][0] not in [0, 1]):
            return "NO"
    
    return "YES"

s = input()
print(check_Lans_lang(s))
