
# (1). Nhập số nguyên tố p: 823
#  (2). Nhập số nguyên tố q: 953
# (3). Nhập khóa công khai e: 313
# (4). Nhập giá trị thông điệp cần gửi:19070
# (5). Khóa được mã hóa là: 160009
# Tài liệu An ninh mạng và An toàn bảo mật hệ thống thông tin, ThS.Nguyễn Văn Hách_nvhach@hunre.edu.vn 18
# (6). Do M = M1, Chấp nhận thông điệp được gửi bởi Alice

def euclid(m, n): 
    if n == 0: 
        return m 
    else: 
        r = m % n 
    return euclid(n, r)
# Thuật toán Euclid mở rộng 
def exteuclid(a, b): 
 #Khởi tạo gán các giá trị 
 n1 = a 
 n2 = b 
 a1 = int(1)
 b1 = int(0)
 a2 = int(0) 
 t2 = int(1)
 while n2 > 0: 
    q = n1//n2 
    n = n1-q * n2 
    n1 = n2 
    n2 = n 
    s = a1-q * a2
    a1 = a2 
    a2 = s 
    t = b1-q * t2 
    b1 = t2 
    t2 = t
 if b1 < 0: 
    b1 = b1 % a 
 return (n1, b1)
#Nhập 2 số nguyên tố p,q
p=int(input("Nhập số nguyên tố p:"))
q=int(input("Nhập số nguyên tố q:"))
e=int(input("Nhập khóa công khai e:"))
M=int(input("Nhập giá trị thông điệp cần gửi:"))
n = p * q 
Pn = (p-1)*(q-1)
# Tạo khóa mã hóa 
# Chọn e sao cho 1<e<Pn 
key = [] 
for i in range(2, Pn): 
 gcd = euclid(Pn, i) 
 if gcd == 1: 
    key.append(i)
# Lựa chọn khóa công khai e 
e = int(e) 
r, d = exteuclid(Pn, e) 
if r == 1: 
 d = int(d) 
 print("Khóa được mã hóa là: ", d) 
else: 
 print("Chọn một khóa mã hóa khác! ")
#Chữ ký số được tạo bởi Alice 
S = (M**d) % n
# Alice gửi tất cả M và S cho Bob 
# Bob tạo thông báo M1 bằng cách sử dụng chữ ký S, khóa công khai của Alice. 
M1 = (S**e) % n 
if M == M1: 
 print("Do M = M1, Chấp nhận thông điệp được gửi bởi Alice") 
else: 
 print("M khác M1,Không được chấp nhận thông điệp được gửi bởi Alice ") 