import random
n=int(input("Nhập số tự nhiên n:")) #100
print("Chương trình dò tìm mật khẩu ngẫu nhiên từ 1 đến",n)
mk = str(random.randint(1,n))
#tạo mảng
ok = " "
while ok != mk:
#tạo các số ngẫu nhiên trong đoạn [1,n]
    ok = str(random.randint(1,n))
#In tất cả các số có thể
print(ok)
#so sánh
if ok == mk:
    print("Mật khẩu tìm được là: "+mk)
    input()