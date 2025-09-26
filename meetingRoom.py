class Solution:
    # @param A : list of list of integers
    # @return an integer
    
    def solve(self, A):
        vRoom=[]
        A.sort()
        print("----->"+ str(A))
        for i in A:
            print("~~"+str(i))
            if len(vRoom) ==0:
                vRoom.append(i[1])
            else:
                for j in range(len(vRoom)):
                    print("~~~~"+str(j)+"~~"+str(vRoom[j]))
                    if vRoom[j] <= i[0]:
                        vRoom[j] = i[1]
                        print("---db1-----")
                        break
                    elif j == len(vRoom)-1 and vRoom[j] > i[0]:
                        vRoom.append(i[1])
                        print("---db2-----")
                    
            print("~vR~"+ str(vRoom))
                

        return vRoom
                
            #print(str(i[0]) +"--"+ str(i[1]) )
            
        
        
A=[[0,30],[15,20],[5,10]]
B=Solution()
print(B.solve(A))

A=[[1, 18], [18, 23], [15, 29], [4, 15], [2, 11], [5, 13]]
B=Solution()
print(B.solve(A))