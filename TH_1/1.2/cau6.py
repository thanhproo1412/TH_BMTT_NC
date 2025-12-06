# 1 # Nhập hai số X và Y dưới dạng chuỗi (cách nhau bởi dấu phẩy)
input_str = input("Nhập X, Y: ")

# 2 # Xử lý đầu vào: tách chuỗi, chuyển thành số nguyên và gán kích thước
dimensions = [int(x) for x in input_str.split(',')]
rowNum = dimensions[0]  # Kích thước hàng (X)
colNum = dimensions[1]  # Kích thước cột (Y)

# 3 # Khởi tạo mảng hai chiều rỗng (danh sách lồng nhau) với kích thước đã cho
# (Dòng này trong hình có vẻ khởi tạo giá trị 0, nhưng cách lặp bên dưới sẽ ghi đè lên)
# Cách khởi tạo tối ưu hơn (như trong hình):
multilist = [[0 for col in range(colNum)] for row in range(rowNum)]

# 4 # Lặp qua các hàng (i) và cột (j) để tính giá trị i * j
for row in range(rowNum):
    for col in range(colNum):
        # Tính giá trị: multilist[i][j] = i * j
        multilist[row][col] = row * col

# 5 # In kết quả mảng hai chiều
print(multilist)