alist=[[87,79,90],[99,83,93],[90,75,89],[89,87,94],[95,85,84]]
for i in range(len(alist)):
    final=int(alist[i][0]*0.6+alist[i][1]*0.3+alist[i][2]*0.1)
    print('the {} final score is {}'.format(i+1,int(final)))