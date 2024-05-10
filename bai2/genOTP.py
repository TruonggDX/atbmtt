import math, random  
def generateOTP() : 
    string ="01234567890123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    OTP = ""
    length = len(string)
    for i in range(8) : 
        OTP += string[math.floor(random.random() * length)] 
    return OTP 

if __name__ == "__main__" : 
 print("Ma OTP:", generateOTP())