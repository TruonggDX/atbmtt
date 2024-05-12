import socket 
# Tạo socket object 
server_address = ('localhost', 5000) 
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
 
# Lắng nghe kết nối tại địa chỉ và cổng được chỉ định
print('starting up on %s port %s' % server_address) 
server_socket.bind(server_address) 
server_socket.listen(1) 
 
# Chờ kết nối từ một client 
print('waiting for a connection') 
client_socket, client_address = server_socket.accept() 
 
# Nhận dữ liệu từ client và gửi lại 
data = client_socket.recv(1024) 
print('received "%s"' % data.decode('utf-8')) 
client_socket.sendall(b'received: ' + data) 
 
# Đóng kết nối 
client_socket.close() 
server_socket.close()