# Biết: 1 pound = 0.453592 kg
# và 1 inch = 2,54 cm
# Viết công thức đổi PSI (Pound / square inches) sang kg/cm2

# INPUT:
# Một con số duy nhất theo đơn vị PSI

# OUTPUT:
# Một con số ương ứng theo đơn vị kg/cm2

# VD:
# 15  ->  1.0546        2018  ->  141.879

input_ = float(input())
a = 0.453592 / (2.54 * 2.54)
result = a * input_
print(result)
