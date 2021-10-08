from fractions import Fraction
n = int(input())
ab = []
for i in range(n):
    _input = input().split()
    ab.append(Fraction(int(_input[0]), int(_input[1])))
for f in ab:
    if (f.denominator == 1):
        print(f.numerator)
    else:
        print(f.numerator, f.denominator)
