'''
文件读写
open：设置权限
read
close
'''

def write():
    # 1、打开文件 1)文件路径，如果不存在，自动创建 2)读写权限
    f=open("test.txt",'a')
    # f = open("test.txt", 'r')
    # 2、写数据
    f.write("abcdfg\n")
    # 3、关闭
    f.close()
# write()

def read():
    f=open("test.txt","r",encoding="utf-8")
    '''
    abcdfgabcdfgabcdfgabcdfgabcdfg
    abcdfg
    abcdfg
    abcdfg
    '''
    result=f.read()
    '''
    abcdfgabcdfgabcdfgabcdfgabcdfg
    '''
    # result=f.readline()
    '''
    ['abcdfgabcdfgabcdfgabcdfgabcdfg\n', 'abcdfg\n', 'abcdfg\n', 'abcdfg\n', 'abcdfg\n']
    '''
    # result=f.readlines()
    print(result)
    f.close()
# read()

#文件备份
def copy():
    oldFileName="test.txt" #--->test_备份.txt
    files=oldFileName.rfind(".")
    oldfileName=oldFileName[:files]
    print("old fileName:",oldfileName)
    last_file=oldFileName[files:]
    print("last fileIndex:",last_file)
    newfileName=oldfileName+"_备份"+last_file
    print(newfileName)
copy()





