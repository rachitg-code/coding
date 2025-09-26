
#User function Template for python3

class Solution:
    iStr=''
    def longestPalin(self, S):
        # code here
        '''cPal=""
        v=""
        lPal=0
        lv=0
        
        pS=0
        pE=0
    
        for i in range(len(S)):
            v=v+i
            lv=lv+1
            if v == v[::-1]:
                if lv > lPal=:
                    cPal=v; lPal=lv
            else:
                lv=0'''
        
        self.iStr=S
        mPalS=''
        
        for i in range(len(S)):
            palS=self.checkPaldm(i)
            if len(mPalS) < len(palS): mPalS=palS
            print(str(i)+"~~"+mPalS)
            
        return mPalS
        
    def checkPaldm(self,j):
        print("<>"+str(j))
        m=self.iStr
        oS=m[j]
        o=j-1
        p=j+1
        
        '''while j-k >=0 and j+k < len(m) and m[j-k] == m[j+k]:
            oS=m[j-k]+oS+m[j+k]
            #print(str(j)+"<>"+str(k)+"<>"+m[j-k]+"<>"+m[j+k]+"<>"+oS)
            
            k=k+1'''
        
        while o >= 0 and p < len(m):
            print(str(j)+"<>"+str(o)+"<>"+str(p)+"<>"+m[o]+"<>"+m[p]+"<>"+oS)
            if m[o] != m[j] and m[j] != m[p] :
                if m[o] == m[p] :
                    oS=m[o]+oS+m[p]
                    o=o-1; p=p+1
                else:
                    break
            else:
                if m[o] == m[j]: 
                    oS=m[o]+oS
                    o=o-1
                if m[j] == m[p]: 
                    oS=oS+m[p]
                    p=p+1
                    
        
        return oS
                


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

        S = 'abc'

        ob = Solution()

        ans = ob.longestPalin(S)

        print(ans)
# } Driver Code Ends