# Your task is to complete this function

class Solution:
    
    #Function to rotate a linked list.
    def rotate(self, head, k):
        # code here
        vN=head
        m=k
        while m >0 :
            if m==1: vPrev=vN
            if vN.next is None:
                vN=head
            else:
                vN=vN.next
            m=m-1
            #print("~~"+str(vN.data))

        
        if vPrev.next != None:
            vPrev.next=None
            vN2=vN
            while vN2.next != None:
                vN2=vN2.next
            vN2.next=head
                #print(str(vPrev.data)+"~~"+str(vN.data))
        head=vN
        
        return head
            



#{ 
 # Driver Code Starts
# driver

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def insert(self,val):
        if self.head is None:
            self.head = Node(val)
            self.tail = self.head
        else:
            self.tail.next = Node(val)
            self.tail = self.tail.next

def printList(n):
    while n:
        print(n.data, end=' ')
        n = n.next
    print()

if __name__=="__main__":
        n = 9
        arr = [int(x) for x in "9 8 6 19 12 3 26 18 5".split()]
        k = 9
        
        lis = LinkedList()
        for i in arr:
            lis.insert(i)
        
        head = Solution().rotate(lis.head,k)
        printList(head)
# } Driver Code Ends