# 1 # Nhập số từ người dùng
# Chuyển đổi dữ liệu nhập vào thành số nguyên (int)
so = int(input("Nhập một số nguyên: "))

# 2 # Kiểm tra xem số đó có phải số chẵn hay không
# Sử dụng toán tử % (chia lấy dư)
if so % 2 == 0:
    print(so, "là số chẵn.")
else:
    print(so, "không phải là số chẵn.")