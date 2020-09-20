'''
9*9乘法表
1*1=1
1*2=2 2*2=4
1*3=3 2*3=6 3*3=9
...
'''

for i in range(1, 10):
    for j in range(1, i+1):
        print('{}x{}={}\t'.format(j, i, i*j), end='')
    print()