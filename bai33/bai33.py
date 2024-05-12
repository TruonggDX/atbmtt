import mysql.connector 
 
# Thông tin kết nối đến cơ sở dữ liệu 
host = "localhost" 
user = "root" 
password = "28042003" 
database = "db_hoadon"
port=3307
 
# Các giá trị cần kiểm tra trong các truy vấn SQL 
payloads =["'", "\"", "--", "#", "/*", "*/", ";"] 
 
# Kết nối đến cơ sở dữ liệu 
conn = mysql.connector.connect(host=host, user=user, password=password, database=database,port=port) 
 
# Lấy danh sách các bảng trong cơ sở dữ liệu 
cursor = conn.cursor() 
cursor.execute("SHOW TABLES;") 
tables = [table[0] for table in cursor.fetchall()] 
 
# Kiểm tra lỗ hổng SQL Injection trên các bảng trong cơ sở dữ liệu 
for table in tables: 
    print("Kiểm tra lỗ hổng SQL Injection trên bảng:", table) 
    # Thực thi các truy vấn SQL với các giá trị kiểm tra 
    for payload in payloads: 
        query = f"SELECT * FROM {table} WHERE column_name = '{payload}'" 
        cursor.execute(query) 
 
        # Kiểm tra xem truy vấn SQL có trả về kết quả hay không 
        result = cursor.fetchone() 
        if result is not None: 
            print("Bảng", table, "có thể bị lỗ hổng SQL Injection với payload:", payload) 
        else:
            print("Bảng", table ,"Khong co lo hong !!!!" )
 
cursor.close() 
conn.close() 