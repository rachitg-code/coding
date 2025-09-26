import re

class Solution:
    def listPerm(self,iL,z):
            oL=[]
            ml=[]
            if len(iL) == 1:
                  #print("~~"+str(z)+"~~"+iL[0]+"~~"+"0~~0")
                  return iL
            else:
                for k in range(len(iL)):

                    nl=list(iL)
                    nl.pop(k)
                    y=z+1
                    '''
                    for t in enumerate(oL):
                        print("..o."+str(z)+"~~"+iL[k]+"~~"+str(t))
                        '''

                    mL= [ iL[k]+x for x in self.listPerm(nl,y) if iL[k]+x not in oL]

                    #for r in enumerate(mL):
                     #   print("..m."+str(z)+"~~"+iL[k]+"~~"+str(r))
                       
                    oL.extend(mL)
                    #print("~~"+str(z)+"~~"+iL[k]+"~~"+str(len(oL))+"~~"+str(len(mL)))

            return oL
    
    def find_permutation(self, S):
        # Code here
        inp=[x for x in S]
        inp.sort()
        for x in self.listPerm(inp,0):
              print(x)

#{ 
 # Driver Code Starts
#Initial Template for Python 3


if __name__ == '__main__':

	S=input()
	ob = Solution()
	ob.find_permutation(S)

# } Driver Code Ends