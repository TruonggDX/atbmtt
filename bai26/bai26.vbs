
Set objShell = CreateObject("WScript.Shell")
Set objFSO = CreateObject("Scripting.FileSystemObject")

' Thiết lập biến để kiểm tra xem chương trình có đang chạy hay không
running = True

' Thiết lập thời gian tự động tắt sau 30 giây
autoShutdownTime = Now + TimeValue("00:00:30")

' Vòng lặp vô hạn để thực hiện các hành động liên tục
Do While running
    ' Gửi phím CAPSLOCK
    objShell.SendKeys "{CAPSLOCK}"
    ' Chờ 1 giây
    WScript.Sleep 1000
    ' Gửi phím NUMLOCK
    objShell.SendKeys "{NUMLOCK}"
    ' Chờ 1 giây
    WScript.Sleep 1000
    ' Gửi phím SCROLLLOCK
    objShell.SendKeys "{SCROLLLOCK}"
    ' Chờ 1 giây
    WScript.Sleep 1000
    ' Gửi phím ENTER
    objShell.SendKeys "{ENTER}"
    ' Chờ 1 giây
    WScript.Sleep 1000
    
    ' Kiểm tra nếu đến thời gian tự động tắt
    If Now >= autoShutdownTime Then
        ' Tắt chương trình
        running = False
    End If
Loop
