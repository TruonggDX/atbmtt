#pip install requests
#pip install beautifulsoup4

import requests 
from bs4 import BeautifulSoup 
 
# URL của trang web cần kiểm tra 
url = "https://www.facebook.com/" 
 
# Các giá trị cần kiểm tra trong URL 
payloads = ["'", "\"", "--", "#", "/*", "*/", ";"] 
 
# Gửi yêu cầu đến trang web với các giá trị kiểm tra 
for payload in payloads: 
    new_url = url + payload 
    response = requests.get(new_url) 
 
    # Phân tích cú pháp HTML của trang web 
    soup = BeautifulSoup(response.text, 'html.parser') 
 
    # Kiểm tra xem trang web có hiển thị lỗi SQL hoặc thông báo lỗi không 
    if "sql syntax" in soup.text.lower() or "syntax error" in soup.text.lower() or "mysql_fetch_array()" in soup.text.lower(): 
        print("Website có thể bị lỗ hổng SQL Injection với payload: " + payload)
    else:
        print("website không có lỗi")