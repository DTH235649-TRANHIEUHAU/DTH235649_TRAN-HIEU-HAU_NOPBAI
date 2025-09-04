t = int(input('Nhap so giay: '))
hour = (t//3600)%24
minute = (t//60)//60
second = (t&3600)%60
print(hour,':',minute,':',second)