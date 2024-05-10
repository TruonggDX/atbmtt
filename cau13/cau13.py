from decimal import Decimal 
#Tìm ước số chung lớn nhất của 2 số
def gcd(a,b): 
    if b==0: 
        return a 
    else: 
        return gcd(b,a%b)
p = int(input('Nhập số nguyên tố p = ')) 
q = int(input('Nhập số nguyên tố q = ')) 
M = int(input('Nhập giá trị bản rõ = '))
n = p*q 
t = (p-1)*(q-1)
#Tính khóa k
for k in range(2,t): 
 if gcd(k,t)== 1: 
    break
for i in range(1,10): 
 x = 1 + i*t 
 if x % k == 0: 
    d = int(x/k) 
 break
#Mã hóa 

mahoa = Decimal(0) 
mahoa =pow(M,k) 
banma = mahoa % n 
#Giải mã
giaima = Decimal(0) 
giaima = pow(banma,d) 
banro = giaima % n 
print('Giá trị của n = '+str(n))
print('Khóa k = '+str(k))
print('Giá trị ϕ(n) = '+str(t))
print('Giá trị của d= '+str(d)) 
print('Bản được mã hóa là = '+str(banma))
print('Bản được giải mã là = '+str(banro))