Set wshShell =wscript.CreateObject("WScript.Shell") 
Tài liệu An ninh mạng và An toàn bảo mật hệ thống thông tin, ThS.Nguyễn Văn Hách_nvhach@hunre.edu.vn 26
do
wscript.sleep 100
wshshell.sendkeys "{CAPSLOCK}"
wshshell.sendkeys "{NUMLOCK}"
wshshell.sendkeys "{SCROLLLOCK}"
 wshshell.sendkeys "~(enter)" 
loop