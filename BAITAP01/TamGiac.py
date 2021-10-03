import math
a = float(input())
b = float(input())
c = float(input())

if (a + b > c and a + c > b and b + c > a):
    if (a == b or b == c or a == c):
        if (a == b and b == c):
            print("Tam giac deu, dien tich = ", end="")
        else:
            print("Tam giac can, dien tich = ", end="")
    elif (a*a == b*b + c*c or b*b == a*a + c*c or c*c == a*a + b*b):
        print("Tam giac vuong, dien tich = ", end="")
    else:
        print("Tam giac thuong, dien tich = ", end="")
    p = (a + b + c) / 2
    area = math.sqrt(p*(p-a)*(p-b)*(p-c))
    area = round(area * 100)
    if (int(area) % 100 == 0):
        print(int(area / 100))
    else:
        print(area / 100)
else:
    print("Khong phai tam giac")
