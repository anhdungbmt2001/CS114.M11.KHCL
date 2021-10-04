# Bình vừa mua xách tay một cái nhiệt kế hồng ngoại cực xịn cực chính xác chỉ mỗi tội
# nó hiển thị nhiệt độ theo thang đo độ F - Farenheit. Hãy giúp Bình đổi qua độ C - Celsius và độ K - Kelvin

# INPUT:
# Một con số - nhiệt độ theo thang F

# OUTPUT:
# Hai con số - nhiệt độ theo thang C và thang K

# VD:
# 658.4  ->  348 621.15        472.6  ->  244.778 517.928

Fah = float(input())
Cel = round((Fah - 32) * (5/9), 3)
Kel = round((Fah + 459.67) * (5/9), 3)
if (int(Cel*10) % 10 == 0):
    Cel = int(Cel)
if (int(Kel*10) % 10 == 0):
    Kel = int(Kel)
print(Cel, Kel)
