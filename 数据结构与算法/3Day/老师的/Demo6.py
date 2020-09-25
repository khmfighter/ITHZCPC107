'''
单链表的实现:
节点和对链表的操作
1.节点:数据和下一个元素的地址
2.链表的操作
  属性:头部指针
  2.1判断链表是否为空
  2.2获取链表的长度
  2.3遍历链表
  2.4头部添加
  2.5尾部追加元素
  2.6指定位置添加元素
  2.7查询指定元素是否存在
  2.8删除指定元素
'''
class Node:
    def __init__(self,item=None):
        self.item = item  #数据
        self.next = None  #指向下一个元素
class Single_Linked:
    def __init__(self):
        self.header = None
    #1.判断链表是否为空
    def isEmpty(self):
        return self.header == None
    #2获取链表的长度
    def length(self):
        count=0
        cur = self.header  #设置临时指针，和头指针一样，指向第一个元素
        while cur != None:
            count+=1
            cur = cur.next
        return  count
    #3遍历链表
    def travel(self):
        cur = self.header
        while cur!=None:
            print(cur.item,end="\t")  #获取当前节点(Node)的值
            cur = cur.next
        print()
    #4头部添加
    def add(self,elem):
        node = Node(elem) #创建节点对象
        if self.isEmpty():
            self.header= node
        else:
            node.next = self.header
            self.header = node
    #5尾部追加元素,如果链表为空，头部添加，否则当临时指针指向最后一个元素
    def append(self,elem):
        if self.isEmpty():
            self.add(elem)   #通过头部方法添加元素
        else:
            node = Node(elem)
            cur =self.header  #临时指针
            while cur.next !=None:
                cur = cur.next
            cur.next = node
    #6指定位置添加元素
    def insert(self,pos,elem):
        if pos<=0:
            self.add(elem)  #头部添加
        elif pos>=(self.length()-1):
            self.append(elem)  #在尾部追加
        else:
            node = Node(elem)
            cur = self.header
            count=0
            while count<(pos-1):
                cur = cur.next #指针向后移
                count+=1
            node.next = cur.next
            cur.next = node

    #7查询指定元素是否存在
    def search(self,elem):
       cur = self.header
       while cur!=None:
           if cur.item == elem:
               return  True
           else:
               cur = cur.next   #指针向下移动
       return  False
    #8删除指定元素
    def remove(self,elem):
        cur = self.heade
        if self.isEmpty():
            return False
        else:
            if cur.item ==elem:  #查找的元素刚好是第一个数据
                self.header= cur.next
                return True
            else:
                while cur.next!=None:  #从第二个元素开始
                   if cur.next.item == elem:
                       cur.next = cur.next.next
                       return  True
                   else:
                       cur=cur.next
                return False
if __name__ =="__main__":
    s = Single_Linked()
  # 1.判断链表是否为空
    print(s.isEmpty())
 #2获取链表的长度
    print("链表长度:",s.length())
    # 4头部添加
    s.add(3)
    s.add(5)
    s.add('a')
    s.travel()   #遍历链表
    # 5尾部追加元素
    s.append('abc')
    s.append('c')
    s.travel()
   #6指定位置添加元素
    s.insert(3,"张三")
    s.travel()
    # 7查询指定元素是否存在
    print(s.search('123'))
    # 8删除指定元素
    print(s.remove('ac'))
    s.travel()