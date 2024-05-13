cls
@ECHO OFF
if EXIST "Control Panel.{21EC2020-3AEA-1069-A2DD-08002B30309D}" goto MO
if NOT EXIST Thumuc goto KHOA
:xacnhan
echo Ban co muon chac chan khoa thu muc nay khong(Y/N)
set/p "cho=>"
if %cho%==Y goto LOCK
if %cho%==y goto LOCK
if %cho%==n goto END
if %cho%==N goto END
echo Lua chon gia tri!.
goto xacnhan
ren Thumuc "Control Panel.{21EC2020-3AEA-1069-A2DD-08002B30309D}"
attrib +h +s "Control Panel.{21EC2020-3AEA-1069-A2DD-08002B30309D}"
echo Thu muc duoc khoa!!!
goto End
:MO
echo Nhap mat khau de mo thu muc
set/p "pass=>"
if NOT %pass%==cntt123@ goto LOI
attrib -h -s "Control Panel.{21EC2020-3AEA-1069-A2DD-08002B30309D}"
ren "Control Panel.{21EC2020-3AEA-1069-A2DD-08002B30309D}" Thumuc
echo Thu muc da duoc mo khoa thanh cong!
goto End
:LOI
echo Mat khau sai!
goto end
:KHOA
md Thumuc
echo Thu muc duoc tao thanh cong!
goto End
:End