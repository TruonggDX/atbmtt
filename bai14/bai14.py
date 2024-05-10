import hashlib
flag=0
dem=0
md5=input("Nhập mảng băm md5 cần giải mã: ") #e16d8f6e68e38c61cf70182c475f386d
file=input("Tên file chứa (tên file.tên mở rộng): ") #đường dẫn của file tudien.txt
try:
    data=open(file,"r")
except:
    print("Không tìm thấy file.")
    quit()
for mk in data:
    mahoa=mk.encode('utf-8')
    bam=hashlib.md5(mahoa.strip()).hexdigest()
    print(mk)
    print(bam)
    print(md5)
    dem+=1
    if bam==md5:
        print("Phá mã MD5 được giải mã.")
        print("Mật khẩu là: "+mk)
        flag=1
        break
if flag==0:
    print("Mật khẩu không tìm thấy được!")