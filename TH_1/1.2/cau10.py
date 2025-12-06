# 1 # Định nghĩa hàm đảo ngược chuỗi
def dao_nguoc_chuoi(chuoi):
    # Sử dụng kỹ thuật cắt lát (slicing) đặc biệt để đảo ngược chuỗi
    return chuoi[::-1]

# 2 # Sử dụng hàm và in kết quả
input_string = input("Mời nhập chuỗi cần đảo ngược: ")
print("Chuỗi đảo ngược là:", dao_nguoc_chuoi(input_string))