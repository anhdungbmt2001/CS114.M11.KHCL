input_ = float(input())
a = (0.453592 / (2.54 * 2.54)) * input_
a = round(a, 6 - len(str(abs(int(a)))))
print(a)
