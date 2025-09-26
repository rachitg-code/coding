"""Return reference of new head of the reverse linked list
  The input list will have at least one element
  Node is defined as

class Node:
    def __init__(self, data):
		self.data = data
		self.next = None
  This is method only submission.
  You only need to complete the method.
"""
import time
class Solution:
    def reverse(self,head, k):
        # Code here
        '''pointer=deque()
        i=head
        j=0
        hf=0
        prevNt=None
        
        while i != None:
            if j<k-1:
                vTemp=i.next.next
                next=i.next
                i.next.next=i
                
                if j==0:
                    prevNt=newTail
                    newTail=i
                i=vTemp
                
                    
                j=j+1
            elif j==k-1:
                j=0
                if hf==0: head =i; hf==1
                else:prevNt.next=i
                '''
                
        i=head
        j=i.next
        l=i.next.next
        m=2
        hf=0
        newHead=head
        
        while i != None:
            print (">>"+str(i.data))
            print (">>m~"+str(m))
            if m==k-1:
                if hf==0: 
                    vHead=l; hf=1
                    print("~~vHead~"+str(vHead.data))
                else:
                    print("deb1")
                    if newHeadPrev != None and l !=None: 
                        print("deb2")

                        newHeadPrev.next=l
                        print("~~newHeadPrev~"+str(newHeadPrev.data))
                        print("~~newHeadPrev.Next~"+str(newHeadPrev.next.data))
            else: 
                if m==0 and l != None: 
                    newHeadPrev=newHead
                    newHead=l
                    newHeadPrev.next=None
                    
                    print("~~newHeadPrev~"+str(newHeadPrev.data))
                    print("~~newHead~"+str(newHead.data))

            if m!= 1: j.next=i
            print("~~>>>"+str(j.data)+"->"+str(j.next.data))

            if m==k-1: m=0
            else: m=m+1
            i=j

            if l !=None:    
                j=l
                print("~~j~"+str(j.data))
            else: 
                if vHead==None: vHead=j
                if newHeadPrev != None and newHeadPrev.next==None:
                    newHeadPrev.next=j
                print(str(vHead.data)+"->"+str(vHead.next.data)+"->"+str(vHead.next.next.data)
                      +"->"+str(vHead.next.next.next.data)+"->"+str(vHead.next.next.next.next.data)
                      +"->"+str(vHead.next.next.next.next.next.data)+"->"+str(vHead.next.next.next.next.next.data))
                newHead.next=None
                
                return vHead
            if l.next!=None: 
                l=l.next
                print("~~l~"+str(l.data))
            else: l=None
            #time.sleep(4)
            
            


#{ 
 # Driver Code Starts
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        # self.tail

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def printList(self):
        temp = self.head
        while (temp):
            print(temp.data, end=" ")
            # arr.append(str(temp.data))
            temp = temp.next
            #time.sleep(1)
        print()

if __name__ == '__main__':
    if True:
        llist = LinkedList()
        n = 1
        #values = [1, 2, 3, 4, 5]
        values =[1]
        for i in reversed(values):
            llist.push(i)
        k = 1
        new_head = LinkedList()
        ob=Solution()
        new_head = ob.reverse(llist.head, k)
        llist.head = new_head
        llist.printList()




# } Driver Code Ends