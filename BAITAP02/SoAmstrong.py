_input = input()
arr_input = []
len_input = len(_input)
for i in range(len_input):
    arr_input.append(int(_input[i]))
sum = 0
for i in arr_input:
    sum += pow(i, len_input)
if (sum == int(_input)):
    print("True")
else:
    print("False")
