# 1 # Nhập số giờ làm việc và mức lương giờ
so_gio_lam = float(input("Nhập số giờ làm mỗi tuần: "))
luong_gio = float(input("Nhập thù lao trên mỗi giờ làm tiêu chuẩn: "))

# 2 # Định nghĩa giờ chuẩn và tính giờ vượt chuẩn
gio_tieu_chuan = 44  # Số giờ làm chuẩn mỗi tuần
# max(0, X) đảm bảo số giờ vượt chuẩn không âm nếu nhân viên làm ít hơn giờ chuẩn
gio_vuot_chuan = max(0, so_gio_lam - gio_tieu_chuan)  # Số giờ làm vượt chuẩn mỗi tuần

# 3 # Tính tổng thu nhập (Lương giờ chuẩn + Lương làm thêm)
thuc_linh = (gio_tieu_chuan * luong_gio) + (gio_vuot_chuan * luong_gio * 1.5)  # Tính tổng thu nhập

# 4 # In kết quả ra màn hình
print(f"Số tiền thực lĩnh của nhân viên: {thuc_linh}")