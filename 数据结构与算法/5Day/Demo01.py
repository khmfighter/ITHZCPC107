'''
树：无序树、有序树、二叉树、完全二叉树、平衡二叉树、排序二叉树
'''
#深度优先遍历
#先根遍历（先序）
#先根节点，再左子节点，最后右子节点

#中根遍历（中序）
#先左子节点，再根节点，最后右子节点

#后跟遍历（后序）
#先左子节点，再右子节点，最后根节点

#广度优先遍历
#从上到下，从左到右


'''
某二叉树的后序遍历序列为：DABEC，中序遍历序列为：DEBAC，则前序遍历为：EDBAC
'''
'''
树的创建和遍历
1、节点
节点数据，左子节点和右子节点

2、添加节点和遍历（广度和深度）
'''
class Node:
    def __init__(self,item):
        self.item=item  #节点数据
        self.lchild=None    #此节点的左子节点
        self.rchild=None    #此节点的右子节点

class Tree:
    def __init__(self):
        self.root=None

    #向二叉树中添加元素
    def add(self,item):
        #判断树中的根是否为空，如果为空，将第一个元素作为根
        node=Node(item)
        queue = []  # 使用队列保存树的结构
        if self.root==None:
            self.root=node
            print("添加根节点：", item)
        else:
            queue.append(self.root)  # 将第一个元素作为根
            while queue:
                cur=queue.pop(0)
                if cur.lchild==None:
                    cur.lchild=node
                    queue.append(node)
                    print("添加左节点：",item)
                    return
                elif cur.rchild==None:
                    cur.rchild=node
                    queue.append(node)
                    print("添加右节点：", item)
                    return
                else:
                    queue.append(cur.lchild)
                    queue.append(cur.rchild)

    #广度优先遍历
    def breath_travel(self,root):
        if root ==None:
            return
        queue=[]
        queue.append(root)
        while queue:
            node=queue.pop(0)
            print(node.item,end=" \t")
            if node.lchild!=None:
                queue.append(node.lchild)
            if node.rchild!=None:
                queue.append(node.rchild)
    #深度优先遍历
    def preorder(self,root):
        if root==None:
            return
        print(root.item,end='\t')
        self.preorder(root.lchild)
        self.preorder(root.rchild)

    # 深度优先遍历
    def midorder(self, root):
        if root == None:
            return

        self.midorder(root.lchild)
        print(root.item, end='\t')
        self.midorder(root.rchild)

    # 深度优先遍历
    def postorder(self, root):
        if root == None:
            return

        self.postorder(root.lchild)
        self.postorder(root.rchild)
        print(root.item, end='\t')

if __name__=='__main__':
    t=Tree()
    t.add('A')
    t.add('B')
    t.add('C')
    t.add('D')
    t.breath_travel(t.root)
    t.preorder(t.root)
    t.midorder(t.root)
    t.postorder(t.root)

#22.前序，中序  B、C
#19.哈夫曼编码，44
'''
19.由带权为9、2、5、7的四个叶子结点构造一棵哈夫曼树，该树的带树路径长度为（D）
A、23            B、37   
C、46            D、44
'''

'''
20.设n，m为一棵树上的两个结点，在中根遍历时，n在m前的条件是（ C ）
A.n在m右方      B.n是m祖先     C.n在m左方      D.n是m子孙
'''

'''
9、C
'''




