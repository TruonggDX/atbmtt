def mahoa(text,k): 
    kq = ""
    #Duyệt chuỗi 
    for i in range(len(text)):
        char = text[i]
    # Kiểm tra các ký tự hoa 
        if (char.isupper()):
            kq += chr((ord(char) + k-65) % 26 + 65)
        #Các ký tự thường 
        else: 
            kq += chr((ord(char) + k - 97) % 26 + 97) 
    return kq
#Nhập nội dung để thực hiện mã hóa 
text = str(input("Nhập chuỗi cần mã hóa(Encrypting):")) #DAIHOCTAINGUYENVAMOITRUONGHANOI
k=int(input("Nhập khóa K cần mã hóa:"))
print ("Bản được mã hóa (Cipher): " + mahoa(text,k))