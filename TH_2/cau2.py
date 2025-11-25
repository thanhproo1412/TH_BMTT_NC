# 1 # Nhập bán kính từ người dùng
# Chuyển đổi dữ liệu nhập vào thành số thực (float) để tính toán
ban_kinh = float(input("Nhập bán kính của hình tròn: "))

# 2 # Tính diện tích của hình tròn
# Công thức: Diện tích = Pi * (bán kính ^ 2)
dien_tich = 3.14 * (ban_kinh ** 2)

# 3 # In diện tích của hình tròn ra màn hình
print("Diện tích của hình tròn là:", dien_tich)