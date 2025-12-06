# 1 # Tạo một danh sách rỗng để lưu kết quả
j = []

# 2 # Duyệt qua tất cả các số trong đoạn từ 2000 đến 3200, kiểm tra
for i in range(2000, 3201):
    # 3 # Kiểm tra điều kiện: chia hết cho 7 (i % 7 == 0) VÀ không phải bội của 5 (i % 5 != 0)
    if (i % 7 == 0) and (i % 5 != 0):
        # 4 # Thêm số đó (chuyển sang chuỗi) vào danh sách
        j.append(str(i))

# 5 # In các phần tử trong danh sách ra màn hình, nối chúng bằng dấu phẩy
print(','.join(j))