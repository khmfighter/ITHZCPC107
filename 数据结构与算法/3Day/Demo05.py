'''
单链表的实现：
节点 Node
1、数据和下一个元素的地址

操作 Operation
1、属性：头部指针
2、方法：（1）判断链表是否为空
        （2）获取链表的长度
        （3）遍历链表
        （4）添加元素（头部）
        （5）添加元素（尾部追加）
        （6）添加元素（指定位置）
        （7）查询指定元素是否存在
        （8）删除指定元素
'''

class Node:
    def __init__(self,item=None):
        self.item=item
        self.next=None

class Single_Linked:
    def __init__(self):
        self.header=None

    # （1）判断链表是否为空
    def isEmpty(self):
        if self.header == None:
            return True
        else:
            return False

    # （2）获取链表的长度
    def length(self):
        count=0
        cur=self.header
        while cur!=None:
            count+=1
            cur=cur.next
        return count

    # （3）遍历链表
    def travel(self):
        cur=self.header
        while cur!=None:
            print("节点值：",cur.item)
            cur=cur.next
    # （4）添加元素（头部）
    def add(self,elem):
        node=Node(elem)
        if self.isEmpty():
            self.header=node
        else:
            node.next=self.header
            self.header=node

    # （5）添加元素（尾部追加）
    def append(self,item):
        if self.isEmpty():
            self.add(item)
        else:
            node=Node(item)
            cur = self.header
            while cur.next != None:
                cur = cur.next
            cur.next=node

    # （6）添加元素（指定位置）
    def insert(self, pos, item):
        if pos<=0:
            self.add(item)
        elif pos>self.length():
            self.append(item)
        else:
            node=Node(item)
            cur=self.header
            count=0
            while count<pos-1:
                cur=cur.next
                count += 1
            node.next=cur.next
            cur.next=node

    # （7）查询指定元素是否存在
    def search(self, item):
        cur = self.header
        while cur != None:
            if cur.item==item:
                return True
            cur = cur.next
        return False

    # （8）删除指定元素
    def delete(self,item):
        pass
if __name__=="__main__":
    s=Single_Linked()
    print(s.isEmpty())
    #头部添加
    s.add(3)
    s.add(5)
    s.add('a')
    #尾部追加
    s.append("b")
    #中间添加
    s.insert(3,'张三')
    #遍历
    s.travel()
    #查询
    print(s.search("d"))
    print("长度为：",s.length())

