import socket 
 
# Tạo socket object 
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
 
# Kết nối đến server 
server_address = ('localhost', 5000) 
print('connecting to %s port %s' % server_address) 
client_socket.connect(server_address) 
 
# Gửi dữ liệu đến server 
message = 'Hello, server. This is client speaking.' 
client_socket.sendall(message.encode('utf-8')) 
 
# Nhận dữ liệu từ server và in ra màn hình 
data = client_socket.recv(1024) 
print('received "%s"' % data.decode('utf-8')) 
 
# Đóng kết nối 
client_socket.close() 