import socket
import subprocess
import sys

subprocess.call('cls', shell=True)
print("CHƯƠNG TRÌNH DÒ QUÉT CÁC CỔNG (PORT) CỦA WEB")

# Nhập địa chỉ IP để quét
temp = input("Nhập địa chỉ IP để quét: ")  #192.168.1.1
try:
    IP = socket.gethostbyname(temp)
except socket.gaierror:
    print("Không thể nhận diện được địa chỉ IP của máy chủ.")
    sys.exit()

# In thông báo chương trình đang quét
print("Vui lòng đợi, đang thực hiện quét địa chỉ IP vừa nhập:", IP)

# Thực hiện quét các cổng đang mở
try:
    for port in range(1, 1025):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((IP, port))
        if result == 0:
            print("Cổng {}: đang mở".format(port))
        sock.close()

except KeyboardInterrupt:
    print("\nQuét cổng đã bị ngắt bởi người dùng.")
    sys.exit()

except socket.error:
    print("Không thể kết nối được đến máy chủ.")
    sys.exit()
