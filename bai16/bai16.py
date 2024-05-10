# 1). Nhập mật khẩu để mã hóa: Hunre123
# (2). Kết quả chuỗi được mã hóa lưu trữ là: 
# f40a2c5237ecc8f0b5bbca4f7605eab8794ccd16e099e2126c4d80c46706a522:5bcf90a8fb004
# 6659c346c66eb26e2d9
# (3). Nhập mật khẩu để kiểm tra lại: Hunre123
# (4). Kết quả trả ra là: Xác thực mật khẩu nhập vào là đúng

import uuid
import hashlib
def hash_password(password):
 # uuid được sử dụng tạo số ngẫu nhiên
 salt = uuid.uuid4().hex
 return hashlib.sha256(salt.encode() + password.encode()).hexdigest() + ':' + salt
def check_password(hashed_password, user_password):
 password, salt = hashed_password.split(':')
 return password == hashlib.sha256(salt.encode() + user_password.encode()).hexdigest()
new_pass = input('Nhập mật khẩu để mã hóa: ')
hashed_password = hash_password(new_pass)
print('Chuỗi được mã hóa lưu trữ là: ' + hashed_password)
old_pass = input('Nhập mật khẩu để kiểm tra lại: ')
if check_password(hashed_password, old_pass):
 print('Xác thực mật khẩu nhập vào là đúng')
else:
 print('Mật khẩu xác thực không đúng')