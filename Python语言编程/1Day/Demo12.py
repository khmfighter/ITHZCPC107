'''
列表生成式
'''

list1=[]
for i in range(10):
    list1.append(i**2)
print(list1)
list1=[i**2 for i in range(10)]
print(list1)