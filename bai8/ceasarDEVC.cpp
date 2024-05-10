#include <iostream> 
using namespace std; 
string mahoa(string text, int k) { 
 string kq = ""; 
 for (int i=0;i<text.length();i++){ 
 if (isupper(text[i])) 
kq += char(int(text[i]+k-65)%26 +65); 
 else
 kq += char(int(text[i]+k-97)%26 +97); 
 } 
 return kq; 
} 
int main() 
{ 
    string text;
    int k; 
    cout << "Nhap chuoi can ma hoa (Encrypting) : "; //ZWDPRDCVCVWTIWDCVIXC
    cin >> text;
    cout << "\nNhap khoa can ma hoa: "; // 15
    cin >> k; 
    cout <<"\nBan duoc ma hoa (Cipher): "<< mahoa(text,k); 
    return 0; 
} 