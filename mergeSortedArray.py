#User function Template for python3

class Solution:
    
    #Function to merge the arrays.
    def merge(self,arr1,arr2,n,m):
        #code here
        i=0; j=0
        oArr=[]
        print(str(n)+str(m)+str(len(arr1))+str(len(arr2)))
        
        while i<n or j<m:
            print("~~"+str(i)+"~~"+str(j)+"~~"+str(oArr))
            if i==n:
                oArr.extend(arr2[j:])
            elif j==m:
                oArr.extend(arr1[i:])
            elif i<n and arr1[i] <= arr2[j]:
                oArr.append(arr1[i])
                i=i+1;
            elif j<m and arr1[i] > arr2[j]:
                oArr.append(arr2[j])
                j=j+1;
                
        arr1=oArr[0:n]
        arr2=oArr[n:]
        
    



#{ 
 # Driver Code Starts
#Initial template for Python

if __name__ == '__main__':
    if True:
        n,m = (4,5)
        arr1 = [1,3,5,7]
        arr2 = [0, 2, 6, 8, 9]
        ob=Solution()
        ob.merge(arr1, arr2, n, m)
        print(*arr1,end=" ")
        print(*arr2)
# } Driver Code Ends