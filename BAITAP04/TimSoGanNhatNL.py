# Cho mảng số nguyên A đã sắp xếp tăng dần, tìm trong mảng k số có giá trị gần với giá trị x nhất.

# INPUT
# Dòng đầu tiên cho biết số phần tử của mảng
# Dòng thứ 2 là toàn bộ mảng liệt kê trên một hàng, các phần tử cách nhau bởi khoảng trắng
# Các dòng sau đó, mỗi dòng chứa 02 số k  và x , k <= n
# Input kết thúc bằng một dòng trống không có nội dung.

# OUTPUT
# Ứng với mỗi cặp số (k, x) xuất ra màn hình số lớn nhất và nhỏ nhất trong dãy k số có giá trị gần với x nhất.
# Nếu có nhiều dãy thõa yêu cầu, xuất ra dãy nằm gần phần đàu mảng A nhất.

# VD
# 15                                        | 27764 27766
# 27753 27754 27755 27756 27758 27758 27760 | 27766 27766
# 27761 27763 27764 27764 27765 27766 27766 | 27760 27766
# 27766                                     | 27753 27766
# 6 43416                                   | 27765 27766
# 3 34222                                   | 27758 27766
# 9 29492                                   |
# 15 10434                                  |
# 4 37086                                   |
# 10 35250                                  |

n = int(input())
a = input().split()
for i in range(n):
    a[i] = int(a[i])
_result = []

while (1):
    x = input()
    if (x == ''):
        break
    x = x.split()
    k = int(x[0])
    x = int(x[1])

    def sort_key(e):
        return abs(e - x)
    a.sort(key=sort_key)
    a_ = a[:k]
    a_.sort()
    _result.append([a_[0], a_[k-1]])
for e in _result:
    print(e[0], e[1])
