#include <iostream> 
using namespace std; 
string giaima(string text, int k) { 
 string kq = ""; 
 for (int i=0;i<text.length();i++){ 
 if (isupper(text[i])) 
kq += char(int(text[i]-k+65)%26 +65); 
 else
 kq += char(int(text[i]-k+97)%26 +97); 
 } 
 return kq; 
} 
int main() 
{ 
 string text;
 int k; 
 cout << "Nhap chuoi can giai ma : ";
 cin >> text;
 cout << "\nNhap khoa can giai ma: ";
 cin >> k; 
 cout <<"\nBan ro duoc giai ma (Decrypting): "<< giaima(text,k); 
 return 0; 
}