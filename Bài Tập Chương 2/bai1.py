import math
try:
    r=float(input('Nhap ban kinh hinh tron: '))
    cv = 2*math.pi*r
    dt = r**2
    print('Chu vi hinh tron la: ', cv)
    print('Dien tich hinh tron la: ', dt)
except:
    print('Loi!')