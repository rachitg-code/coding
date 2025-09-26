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
        
        i=head
        j=i.next
        m=0
        n=m
        
        hf=0
        
        vTail=None
        vHead=head
        
        o=None
        
        while i !=None :

            print(str(m)+"~~"+str(n))
            print(">>"+str(i.data)+"--"+str(vHead.data)+"--"+str(hf))
            

            if m > 12 : 
                print("m limit exceeded")
                break

            if hf==0: vHead=i
            
            if j !=None:

                print("--"+str(j.data))
                
                if j.next == None:
                    l=None
                else:
                    l=j.next
                    print(">> l :"+str(l.data)) 
                
                if n!=k-1: j.next=i
            else:
                print("--"+"j is None")
                l=None
            
            if n==0:
                vTailPrev=vTail
                vTail=i
                i.next=None
            if n==k-1 or j==None:
                if hf==0:
                    hf=1
                else:
                    vTailPrev.next=i
                    print(">><<"+str(vTailPrev.data)+"--"+str(vTailPrev.next.data))
            
            i=j
            j=l
            m=m+1
            n=m%k

        return vHead
            
            

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
            time.sleep(1)
        print()

if __name__ == '__main__':
    if True:
        llist = LinkedList()
        n = 1
        #values = [1, 2, 3, 4, 5]
        #values =[1]
        #values =[1, 2, 2, 4, 5, 6, 7, 8]
        values = [4, 7, 1]
        for i in reversed(values):
            llist.push(i)
        k = 3
        new_head = LinkedList()
        ob=Solution()
        new_head = ob.reverse(llist.head, k)
        llist.head = new_head
        llist.printList()




# } Driver Code Ends