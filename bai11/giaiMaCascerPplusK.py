def giaima(text,k): 
    kq = ""
    #Duyệt chuỗi 
    for i in range(len(text)):
        char = text[i]
        # Kiểm tra các ký tự hoa 
        if (char.isupper()):
            kq += chr((ord(char) - k-65) % 26 + 65)
        #Các ký tự thường 
        else: 
            kq += chr((ord(char) - k - 97) % 26 + 97) 
    return kq
#Nhập nội dung bản mã C để thực hiện giải mã 
text = str(input("Nhập chuỗi cần giải mã(Decrypting):"))
k=int(input("Nhập khóa K cần giải:"))
print ("Bản rõ được giải (Text): " + giaima(text,k))