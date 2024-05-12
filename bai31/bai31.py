import subprocess 
 
result = subprocess.run(["netsh", "wlan", "show", "interfaces"], capture_output=True, 
text=True) 
 
if result.returncode == 0: 
    print(result.stdout) 
else: 
    print("Lỗi: Không thể hiển thị card WLAN.")