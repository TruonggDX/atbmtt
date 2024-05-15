import random
import string

def generate_otp(length):
    characters = string.ascii_letters + string.digits
    otp = ''.join(random.choice(characters) for _ in range(length))
    return otp

otp = generate_otp(8)
print("Mã OTP được tạo:", otp)
