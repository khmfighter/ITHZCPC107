'''
单向循环链表
1.节点:元素和下指针
2.链表操作
   1.判断是否为空
   2.获取链表长度
   3.遍历链表
   4.头部添加
   5.尾部追加
   6.指定位置添加
   7.查询
   8.删除
'''
class Node:
    def __init__(self,item):
        self.item = item
        self.next = None
class Circle_Linked:
    def __init__(self):
        self.header = None
    #1.判断是否为空
    def isEmpty(self):
        return  self.header==None
    #2.获取链表长度
    def length(self):
       if self.isEmpty():
           return 0
       count =1
       cur = self.header
       while cur.next!=self.header:
           cur = cur.next
           count+=1
       return  count
    #3.遍历链表
    def travel(self):
        if self.isEmpty():
            return
        cur = self.header
        while cur.next!=self.header:
            print(cur.item,end="\t")
            cur = cur.next
        print(cur.item)
    #4.头部添加
    def add(self,item):
        node = Node(item) #创建节点
        if self.isEmpty():
            self.header = node
            self.header.next = self.header
        else:
            cur = self.header
            while cur.next!=self.header:
                cur = cur.next
            cur.next = node
            node.next=self.header
            self.header = node

    #5.尾部追加
    def append(self,item):
          if self.isEmpty():
              self.add(item)  #如果链表为空，直接头部添加
          else:
              cur  = self.header
              while cur.next !=self.header:
                  cur = cur.next
              #循环结束后，临时指针cur执行最后一个元素
              node = Node(item)
              cur.next = node
              node.next = self.header

    #6.指定位置添加
    def insert(self,pos,item):
        if pos<=0:
            self.add(item)
        elif pos>=(self.length()-1):
            self.append(item)
        else:
            count =0
            cur = self.header
            while count <(pos-1):
                cur = cur.next
                count+=1
            node = Node(item)
            node.next = cur.next
            cur.next = node
    #7.查询
    def search(self,item):
       if self.isEmpty():
           return False
       else:
           if self.header.item == item:
               return True
           else:
               cur = self.header
               while cur.next!=self.header:
                   if cur.next.item == item:
                       return  True
                   else:
                       cur = cur.next
               return  False

    #8.删除
    def delete(self,item):
        if self.isEmpty():
            return  False
        if self.header.item==item:
            if self.length()==1:
                self.header = None
                return True
            else:
                cur = self.header
                while cur.next!=self.header:
                    cur = cur.next
                #指针指向最后一个元素
                self.header = self.header.next
                cur.next = self.header
                return True
        else:
            cur = self.header
            while cur.next != self.header:
                if cur.next.item == item:
                    cur.next = cur.next.next
                    return True
                else:
                    cur = cur.next
            return False
if __name__ =="__main__":
    s = Circle_Linked()
    s.travel()
    s.add(123)
    s.add('A')
    s.add('B')
    s.travel()
    print(s.length())
    #尾部追加
    s.append("345")
    s.travel()
    #指定位置添加
    s.insert(12,"ABC")
    s.travel()
    print(s.search('ABC'))
    s.delete(123)
    s.travel()



