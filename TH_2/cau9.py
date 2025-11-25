# 1 # Hàm kiểm tra số nguyên tố
def kiem_tra_so_nguyen_to(n):
    # Điều kiện 1: Số nguyên tố phải lớn hơn 1
    if n <= 1:
        return False
    
    # Điều kiện 2: Kiểm tra sự chia hết từ 2 đến căn bậc hai của n
    # int(n ** 0.5) + 1 tương đương với việc lấy phần nguyên của căn(n) và thêm 1
    for i in range(2, int(n ** 0.5) + 1):
        # Nếu n chia hết cho bất kỳ số nào trong khoảng này, nó không phải là số nguyên tố
        if n % i == 0:
            return False
            
    # Nếu vượt qua tất cả các kiểm tra, nó là số nguyên tố
    return True

# 2 # Kiểm tra số nguyên tố và in kết quả
number = int(input("Nhập vào số cần kiểm tra: "))
if kiem_tra_so_nguyen_to(number):
    print(number, "là số nguyên tố.")
else:
    print(number, "không phải là số nguyên tố.")