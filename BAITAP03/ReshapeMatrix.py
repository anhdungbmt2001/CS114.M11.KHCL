# Cho một ma trận có kích thước mxn và hai biến r,c tương ứng với số dòng và số cột muốn reshape.
# Ma trận được reshape có kích thước rxc và được điền đầy đủ các phần tử của ma trận gốc theo chiều ngang.
# Nếu có thể reshape được ma trận, xuất ra ma trận mới. Ngược lại, xuất ma trận gốc.

# INPUT:
# Dòng đầu tiên gồm hai số nguyên dương n, m (2 <= n, m <= 3000) - Theo thứ tự là số hàng, cột của ma trận gốc.
# Dòng thứ hai gồm hai số nguyên dương r, c - Theo thứ tự là số hàng, cột của ma trận muốn reshape thành.
# n dòng tiếp theo là giá trị từng hàng của ma trận gốc a1,a2,...,am (−105 <= ai <= 105) - Các phần tử
# cách nhau một khoảng trắng.

# OUTPUT:
# Nếu có thể reshape được ma trận, xuất ra ma trận mới. Ngược lại, xuất ma trận gốc.
