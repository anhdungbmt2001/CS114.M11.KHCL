Fah = float(input())
Cel = (Fah - 32) * (5/9)
Cel = round(Cel, 6 - len(str(abs(int(Cel)))))
Kel = (Fah + 459.67) * (5/9)
Kel = round(Kel, 6 - len(str(abs(int(Kel)))))
if (int(Cel*10) % 10 == 0):
    Cel = int(Cel)
if (int(Kel*10) % 10 == 0):
    Kel = int(Kel)
print(Cel, Kel)
