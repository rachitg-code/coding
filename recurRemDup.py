#User function Template for python3

class Solution:
    def rremove (self, S):
		#code here
		#cS=S[0]
        i=0
		#oS=rrem(S,cS,i)
        oS=self.rrem(S,i)

        return oS[oS.index("]")+1:] if "]" in oS else oS
		
		
		
    '''def rrem(self, S, cS, i):
    
        subS=rrem(S,cS,i+1)
        if S[i] != subS[0]:
            return S[i]+subS
        else:
            return subS'''
            
    '''def rrem(self, S, i):
        if i==len(S)-1: return S[-1]
        else :
            subS=self.rrem(S,i+1)
            if S[i] != subS[0]:
                return S[i]+subS
            else:
                return subS'''
                
    def rrem(self, S, i):
        
        if i==len(S)-1: return S[-1]
        else :
            subS=self.rrem(S,i+1)
            
            print("~~"+str(i)+subS)
            if subS[0] == "[": 
                if S[i] == subS[1]: return  "["+S[i]+subS[1:]
                elif S[i] != subS[1]: 
                    subS=subS[subS.index("]"):]
                    subS=subS.replace("]","")
                
            if len(subS) ==0 or S[i] != subS[0]:
                return S[i]+subS
            else:
                return "["+ S[i]+subS[0]+"]"+subS[1:]
	        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
 
    S = 'acaaabbbacdddd'
    ob = Solution()
    print(ob.rremove(S))


# } Driver Code Ends