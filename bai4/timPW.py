from random import randint

mk = input("Nhập mật khẩu cần tìm: ")

# Lập dãy các kí tự bảng Alpha, bao gồm cả chữ thường và hoa
Alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 
         'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
         'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 
         'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 
         'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

find_pass = ""

while find_pass != mk:
    find_pass = ""
    
    # Tạo mật khẩu ngẫu nhiên từ bảng Alpha có cùng độ dài với mk
    for _ in range(len(mk)):
        find_pass += Alpha[randint(0, len(Alpha) - 1)]
    
    # In ra mật khẩu được tạo trong quá trình kiểm tra
    print(find_pass)

print("Mật khẩu của bạn được tìm thấy:", find_pass)
