text= "UHNIUHPUVUIGUNNBIHANCH"
Alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
for key in range(len(Alpha)):
    s = ''
    for i in text:
        if i in Alpha:
            num = Alpha.find(i)
            num = (num - key) % len(Alpha)
            s = s + Alpha[num]
        else:
            s = s + i
    print("Khóa cần tìm K=%s: %s" % (key,s))