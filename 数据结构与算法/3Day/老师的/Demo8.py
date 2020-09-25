'''
双链表
1.节点:
  属性:数据,上指针，下指针
2.链表操作
   属性:头指针
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
        self.prev = None   #上指针
        self.next = None   #下指针
class Double_Linked:
    def __init__(self):
        self.header =None
    #1.判断是否为空
    def isEmpty(self):
       return  self.header==None
    #2.获取链表长度
    def length(self):
       count = 0
       cur = self.header
       while cur!=None:
           count+=1
           cur = cur.next
       return  count
    #3.遍历链表
    def travel(self):
        if self.isEmpty():
            return
        cur = self.header
        while cur != None:
            print(cur.item,end="\t")
            cur = cur.next
        print()
   #4.头部添加
    def add(self,item):
        node =Node(item)
        if self.isEmpty():
            self.header =node
        else:
            node.next = self.header
            self.header.prev = node
            self.header = node
   #5.尾部追加
    def append(self,item):
        if self.isEmpty():
            self.add(item)
        else:
            cur = self.header
            node = Node(item)
            while cur.next!=None:
                cur = cur.next
            cur.next = node
            node.prev = cur
    #6.指定位置添加
    def insert(self,pos,item):
        if pos<=0:
            self.add(item)
        elif pos>=(self.length()-1):
            self.append(item)
        else:
            count =0
            cur = self.header
            while count<(pos-1):
                count+=1
                cur = cur.next
            #指针指向添加元素小标的上一个元素
            node = Node(item)
            node.next = cur.next
            node.prev = cur
            cur.next.prev = node
            cur.next = node
   #7.查询
    def search(self,item):
        if self.isEmpty():
            return False
        else:
            cur = self.header
            while cur!=None:
                if cur.item ==item:
                    return True
                else:
                    cur = cur.next
            return False
   #8.删除
    def remove(self,item):
       if self.isEmpty():
           return False
       else:
           if self.header.item ==item:
               if self.length()==1:
                  self.header = None

               else:
                   self.header = self.header.next
                   self.header.prev = None
               return True
           else:
               cur = self.header
           while cur!=None:
               if cur.item == item:
                   cur.prev.next = cur.next
                   if cur.next!=None:
                       cur.next.prev =cur.prev
                   else:
                       cur.prev = None
                   return True
               else:
                   cur = cur.next
           return False
if __name__ =="__main__":
    s = Double_Linked()
    s.add("234")
    s.travel()
    s.add("2")
    s.add("3")
    s.travel()
    s.append(567)
    s.travel()
    s.insert(2,"abc")
    s.insert(3,"abc")
    s.travel()
    print(s.remove(567))