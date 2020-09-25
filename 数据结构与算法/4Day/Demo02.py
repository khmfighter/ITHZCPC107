'''
栈
顺序表实现（list）
1、创建栈
2、添加元素，在栈顶添加
3、删除元素，在栈顶删除
4、获取栈的长度
5、判断元素是否存在
6、获取栈顶元素(pop)
7、判断栈是否为空
'''

class Stack:
    #初始化栈
    def __init__(self):
        self.lists=[]

    #判断栈是否为空
    def isEmpty(self):
        return self.lists==[]

    #添加元素
    def add(self,item):
        self.lists.append(item)

    #删除栈顶元素
    def remove(self):
        self.lists.pop()

    #获取栈的长度
    def length(self):
        return len(self.lists)

    #判断元素是否存在
    def isExist(self,item):
        return item in self.lists

    #获取栈顶元素
    def getPopItem(self):
        return self.lists[-1]


if __name__=="__main__":
    stack=Stack()
    stack.add(1)
    stack.add(2)
    stack.add(4)

    print(stack.lists)
    print(stack.getPopItem())
    print(stack.remove())
    print(stack.lists)
