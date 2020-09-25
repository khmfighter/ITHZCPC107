'''
Queue队列
先进先出的数据结构
1、创建队列
2、判断队列是否为空
3、在尾部追加元素
4、在头部删除元素
5、遍历队列
6、获取队列的长度
'''

class Queue:
    # 1、创建队列
    def __init__(self):
        self.lists=[]

    # 2、判断队列是否为空
    def isEmpty(self):
        return self.lists==[]

    # 3、在尾部追加元素
    def append(self,item):
        self.lists.append(item)

    # 4、在头部删除元素
    def delete(self):
        self.lists.pop(0)

    # 5、遍历队列
    def travel(self):
        print(self.lists)

    # 6、获取队列的长度
    def length(self):
        return len(self.lists)

if __name__=="__main__":
    q=Queue()
    print(q.isEmpty())
    q.append("a")
    q.append("b")
    q.append("c")
    q.append("d")
    q.travel()
    q.delete()
    q.travel()