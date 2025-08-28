def in_cay_thong():
    #Tang 1
    for i in range(1,4,2):
        print(' ' * (4 - i) + '*' * i)

    #Tang 2
    for i in range(3,8,2):
        print(' ' * (6 - i) + '*' * i)

    #Tang 3
    for i in range(3,12,2):
        print(' ' * (8 - i) + '*' * i)

    #Than cay 
    for i in range(2):
        print(' ' * 3 + '***')

in_cay_thong() 