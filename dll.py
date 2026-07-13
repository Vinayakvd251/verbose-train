
class node:
    def __init__(self,data=None):
        self.data=data
        self.prev=None
        self.next=None
class DoubleLinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
    def InsertAtEnd(self,data):
        newnode=node(data)
        if self.head==None and self.tail==None:
            self.head=self.tail=newnode
        newnode.prev=self.tail
        self.tail.next=newnode
        self.tail=newnode
    def DeleteAtEnd(self):
        if self.head is None:
            print("list is empty,cant delete")
        elif self.head==self.tail:
            print("deleted node",self.tail.data)
            self.head=self.tail=None
        else:
            print("deleted node",self.tail.data)
            self.tail=self.tail.prev
            self.tail.next=None
        return
    def traverse(self):
        if self.head is None:
            print("list is empty,cant delete")
        else:
            print("list item")
            t=self.head
            while(t):
                print(t.data)
                t=t.next
        return
DLL=DoubleLinkedList()
DLL.DeleteAtEnd()
DLL.traverse()
DLL.InsertAtEnd(100)
DLL.InsertAtEnd(200)
DLL.InsertAtEnd(300)
DLL.DeleteAtEnd()
DLL.traverse()



