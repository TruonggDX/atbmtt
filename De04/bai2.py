import socket
import sys

def port_scan(target):
    try:
        for port in range(1, 1025):
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(0.1)
            result = s.connect_ex((target, port))
            if result == 0:
                print(f"Cổng {port} đang mở")
            s.close()
    except KeyboardInterrupt:
        print("\n Thoát .")
        sys.exit()
    except socket.gaierror:
        print("Không tìm thấy")
        sys.exit()
    except socket.error:
        print("Không thể kết nối")
        sys.exit()

if __name__ == "__main__":
    target = input("Nhập địa chỉ ip hoặc trang web: ")  #Nhập hunre.edu.vn
    port_scan(target)