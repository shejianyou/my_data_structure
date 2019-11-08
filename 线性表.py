# -*- coding: utf-8 -*-
"""
Created on Mon Nov 4 21:05:43 2019

@author: 佘建友

"""
class LinkedlistUnderflow(ValueError):
    pass


#the signal linked-list
class LNode:
    def __init__(self, elem, next_=None):#the 'Next' addes '_' have no sepcal meaning!
        self.elem = elem
        self.next = next_

class LList(LNode):
    def __init__(self):
        self._head = None
    
    def is_empty(self):
        return self._head is None
    
    def count(self,x):
        """
        type x = any type
        this function returns the count of a special and given elem.
        """
        p = self._head
        count = 0
        while p is not None:
            if x == p.next:
                count += 1
        return count
    
    def printall(self):
        p = self._head
        while p is not None:
            print(p.elem, end = '')
            if p.next is not None:
                print(', ', end='')
            p = p.next
        print('')
    
    def for_each(self, proc):
        p = self._head
        while p is not None:
            proc(p.elem)
            p = p.next
    
    def find(self, pred):
            p = self._head # point to the next
            while p is not None:
            if pred(p.elem):
                return p.elem
            p = p.next

    def elements(self):
        """
to define a generator,this idea bases on the need to get every element at relexity.
        """
        p = self._head
        while p is not None:
            yield p.elem
            p = p.next

    @staticnethod
    def length(self,head):
        """
        """
        p, num = head, 0
        while p is not None:
            n += 1
            p = p.next
        return num
    def __equal__(self,another):
        p = self._head
        q = another._head
        n = 0
        length = min(self._length(self,head),another._length(another,head))
        while p is not None and i < length :
            i = i-1
            x = self._head.next
            y = another._head.next
            m = x == y
            n += m
        if n == length:
            print (True)
        else:
            print(False)
    
    def __big__(self,another):
        p = self._head
        q = another._head
        length = min(self._length(self,head),another._length(another,head))
        for i in range(0,length-1):
            x = str(p.next)
            y = str(q.next)
            if x > y:
                print(True)
                break
    
    def __small__(self,another):
        p = self._head
        q = another._head
        length = min(self._length(self,head),another._length(another,head))
        for i in range(0,length-1):
            x = str(p.next)
            y = str(q.next)
            if x < y:
                print(True)
                break
    
    def __small_and_equal_(self,another):
        """
i believe this program is not the last script,maybe it is not the best way to solve this problem.
        """
        p = self._head
        q = another._head
        length = min(self._length(self,head),another._length(another,head))
        for i in range(0,length-1):
            x= str(p.next)
            y = str(q.next)
            if x <= y:
                print(True)
                break
            
    
    def __small_and_equal_(self,another):
        p = self._head
        q = another._head
        length = min(self._length(self,head),another._length(another,head))
        for i in range(0,length-1):
            x= str(p.next)
            y = str(q.next)
            if x >= y:
                print(True)
                break
   
    def prepend(self, elem):
        self._head = LNode(elem, self._head)
        num = num-1
        return num

    def pop(self):
        if self._head is None:  #if it have no node,there is a exception which i have defined.
            raise LinkedlistUnderflow("in pop")
        e = self._head.elem
        self._head = self._head.next
        return e
        num = num - 1
        return num 
        
    def append(self, elem):
        if self._head is None:
            self._head = LNode(elem)
            return 
            p = self._head
            while p.next is not None:
                p = p.next
                p.next = LNode(elem)
        num = num - 1
        return num
            
    def pop_list(self):
        if self._head is None: #an empty list
            raise LinkedlistUnderflow("in pop_last")
        p = self._head
        if p.next is None:  #an list which inclueds an elem
            e = p.elem
            self._head = None
            return e
            num = num - 1
            return num
        while p.next.next is not None: #the p.next is the last node
            p = p.next
            e = p.next.elem
            p.next = None
            return e
            num = num - 1
            return num

    def del_i(self,i=None):
        p = self._head
            if i >= 0:
                while p is not None:
                    i -= 1
                    p = p.next
                e = p.next.elem
                p.next = p.next.next
                num = num - 1
                return e

            else:
                i = num + i
                while p is not None:
                    i -= 1
                    p = p.next
                    e = p.next.elem
                    p.next = p.next.next
                    num = num - 1
                return e 
                     
        def insert_i(self,elem,i=None):
            p = self._head
            if self.is_empty:
                p.next = elem
                while p is not None and i == 1:
                    i -= 1
                    p = p.next
                return LNode(elem,p)
            
    def create_linkedlist(self,d):#type d = list[objects]
        p = self._head
        self._head = d
        for i in range(0,len(d)-1):
            elem = d[i]
            class LNode(p,d[i])
            i += 1
            p = self._head.next
            self._head.next = d[i+1]
        return p

    def create_sequence(self):
        p = self._head
        d = []
        while p is not None:
            d = d.append(p.next)
            p = p.next
        return d 
    
    def rev_visit(self):
        d = create_sequence(self).sort(reverse=True)
        p = self._head
        self._head = d
        for i in range(0,len(d)-1):
            elem = d[i]
            i += 1
            p = p.next
            p.next = d[i+1]
        return p 
    
    def del_minial(self):
        LList = self.creat_sequence(self).sort()#the while loop means the price of time increses with the quatantiy of elems
        p = self._head
        self._head = LList
        for i in range(0,len(LList)-1): # the price of time is the O(n)
            if LList[0] == LList[i]:
                LList = LList.remove(LList[i])
        return self.create_linkedlist(self,LList) # the price of the time is the O(n)
    
    def del_if(self,pred):
        p = self._head
        while p is not None:
            if pred(p.next.elem):
                p.next = p.next.next
        return self.__init__(self)
    
    def del_duplicate(self):
        p = self._head
        while p is not None: # the price of time is the O(n)
            if p.next == self.next:
                p.next == p.next.next
        return self.__init__(self)
    
    def interleaving(self, another):
        self_len = len(self.create_sequence(self))
        another_len = len(another.create_sequence(another)) 
        my_list = []
        if self_len == another_len:  # the price of time is at least the O(n**2)
            for i in range(0,self_len):
                my_list = my_list.append(self.create_sequence[i])
                for j in range(0,another_len):
                    my_list = my_list.append(another.create_sequence[j])
                    break
        return my_list
        if self_len < another_len:
            for i in range(0,self_len):
                d = d.append(self.my_list[i])
                for j in range(0,another_len):
                    my_list = my_list.append(another.create_sequence(another)[j])
                    break
        my_list = my_list.extend(another.create_sequence(another)[self_len:another_len])
        return my_list
        if self_len > another_len:
            for i in range(0,another_len):
                my_list = my_list.append(another.create_sequence(another)[i])
                for j in range(0,self_len):
                    my_list = my_list.append(self.create_sequecne(self)[i])
                    break
        my_list = my_list.extend(self.create_sequence(self)[another_len:self_len])
        return my_list



class LList1(LList):
    def __init__(self):
        LList.__init__(self)
        self._rear = None # the last field

    def prepend(self,elem):
        if self._head == None: #it's an empty LList
            self._head = LNode(elem,self._head)
            self._rear = self._head
        else:
            self._head = LNode(elem, self._head)
        
    def append(self,elem):
        if self._head is None:#it's an empty LList
            self._head = LNode(elem,self._head) #add an elem
            self._rear = self._head
        else:
            self._rear.next = LNode(elem,next=None)
            self._rear = self._rear.next
    
    def pop_list(self):
        if self._head is None: #an empty list
            raise LinkedlistUnderflow("in pop_last")
        p = self._head
        if p.next is None:  #an list which inclueds an elem
            e = p.elem
            self._head = None
            return e
            num = num - 1
            return num
        while p.next.next is not None: #the p.next is the last node
            p = p.next
            e = p.next.elem
            p.next = None
            return e
            num = num - 1
            return num

    def pop_last(self):
        if self._head is None:
            raise LinkedlistUnderflow('in pop_last')
        p = self._head
        if p.next is None:
            e = p.elem
            self._head = None
            return e
        while p.next.next is not None:
            p = p.next
        e = p.next.elem
        p.next = None
        self._rear = p
        return e
    
class LClist(LNode):#循环单链表
    def __init__(self):
        self._rear == None 
    
    def is_empty(self):  #判断是否为空表
        return self._rear == None
    
    def prepend(self,elem):    #前端插入
        P = LNode(elem)
        if self._rear == None:
            p.next = p
            self._rear = p
        else:
            p.next = self._rear.next
            self._rear.next = p 
    
    def append(self,elem):      #尾端插入
        self.prepend(elem)
        self._rear = self._next.next
                
    def pop(self):             #前端弹出
        if self._rear is None:
            raise LinkedlistUnderFlow("in pop of CLList")
        p = self._rear.next
        if self._rear is p:
            self._rear = None
        else: 
            self._rear.next = p.next

        return p.elem

    def printall(self):        #输出元素
        """
if the self._rear is not None,the self._rear have no None value forever.
so i can set the None to self._None,
attention,i have no aware on the zero llclist
        """
        if self.is_empty():
            return
        p = self._rear.next
        while True:
            print(p.elem)
            if p is self._rear:
                break
            p = p.next

class DLNode(LNode):
    def __init__(self, elem, prev=None, next_=None):
        LNode.__init__(self,elem,next_)
        self.prev = prev
class DLList(LList1):
    def __init__(self):
        LList1.__init__(self):
    
    def prepend(self, elem):
        p = DLNode(self,elem,self._rear=None):
        if self._head is None:
            self._rear = p
        else:
            p.next.prev = p
        self._head = p
    
    def append(self,elem):
        p = DLNode(elem, self._rear, None)
        if self._head is None:
            self._head = p
        else:                  #非空表，设置next引用
            p.next.prev = p
        self._rear = p
    
    def pop(self):
        if self._head is None:
            raise LinkedlistUnderflow("in pop of DLList")
        e = self._self._head.elem
        self._head = self._head.next
        if self._head is not None:  #
            self._head.prev = None
        return e
    
    def pop_last(self):
        if self._head is None:
            raise LinkedlistUnderflow("in pop_last of DLList")
        e = self._rear.elem
        self._rear = self._rear.prev
        if self._head is not None:
            self._head.prev = None
        return e
    
    def pop_last(self):
        if self._head is None:
            raise LinkedlistUnderflow('in pop_last of DLList')
        e = self._rear.elem
        self._rear = self._rear.prevt
        if self._rear is None:
            self._head = None
        else:
            self._rear.next = None
        return e
    
    

    




    






        
        

            

                

            







        
        

        

        
        
            


        
            







            



   