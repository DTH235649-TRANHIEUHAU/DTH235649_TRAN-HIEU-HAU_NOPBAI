import sys
#sys.argv la danh sach cac tham so dong lenh
#sys.argv[0] la ten file .py
#sys.argy[1:] la cac tham so nhap them

if len(sys.argv) > 1:
    #Ghep cac tham so thanh 1 chuoi
    chuoi = " ".join(sys.argv[1:])
    print("Chuoi ky tu vua nhap la:", chuoi)
else:
    print("Ban chua nhap chuoi nao!")