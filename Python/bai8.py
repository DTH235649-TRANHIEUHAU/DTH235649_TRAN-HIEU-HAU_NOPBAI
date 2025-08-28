def hcn_rong(n,m):
    for i in range(n):
        for j in range(m):
            if i == 0 or i == n - 1 or j == 0 or j == m-1:
                print('*',end='')
            else:
                print(' ', end='')
        print()

hcn_rong(5,5)
