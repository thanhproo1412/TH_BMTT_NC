# 1 # Hàm kiểm tra số nhị phân có chia hết cho 5 không
def chia_het_cho_5(so_nhi_phan):
    # Chuyển số nhị phân sang số thập phân (cơ số 2)
    so_thap_phan = int(so_nhi_phan, 2)
    
    # Kiểm tra xem số thập phân có chia hết cho 5 không
    if so_thap_phan % 5 == 0:
        return True
    else:
        return False

# 2 # Nhập chuỗi số nhị phân từ người dùng
chuoi_so_nhi_phan = input("Nhập chuỗi số nhị phân (phân tách bởi dấu phẩy): ")

# 3 # Tách chuỗi, kiểm tra và lọc các số thỏa mãn điều kiện
so_nhi_phan_list = chuoi_so_nhi_phan.split(',')
# Lọc các số nhị phân chia hết cho 5 bằng cách gọi hàm
so_chia_het_cho_5 = [so for so in so_nhi_phan_list if chia_het_cho_5(so)]

# 4 # In ra các số nhị phân chia hết cho 5
if len(so_chia_het_cho_5) > 0:
    # Nối các số nhị phân bằng dấu phẩy để in ra
    ket_qua = ','.join(so_chia_het_cho_5)
    print("Các số nhị phân chia hết cho 5 là:", ket_qua)
else:
    print("Không có số nhị phân nào chia hết cho 5 trong chuỗi đã nhập.")