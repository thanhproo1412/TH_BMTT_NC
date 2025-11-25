# 1 # Nhập các dòng từ người dùng
print("Nhập các dòng văn bản (Nhập 'done' để kết thúc):")
lines = []

# 2 # Vòng lặp liên tục để nhận các dòng đầu vào
while True:
    line = input()
    # Kiểm tra xem người dùng có nhập 'done' để kết thúc không
    if line.lower() == 'done':
        break
    
    # Thêm dòng vừa nhập vào danh sách
    lines.append(line)

# 3 # Chuyển các dòng thành chữ in hoa và in ra màn hình
print("\nCác dòng đã nhập sau khi chuyển thành chữ in hoa:")
for line in lines:
    # Sử dụng phương thức .upper() để chuyển chuỗi thành chữ hoa
    print(line.upper())