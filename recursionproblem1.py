#recursionproblem1
#print-1-to-n-without-using-loops
#link: https://www.geeksforgeeks.org/problems/print-1-to-n-without-using-loops-1587115620/1



#User function Template for python3

class Solution:    
    #Complete this function
    def printNos(self,n):
        if n<1:
            return
        else:
            self.printNos(n-1)
            print(n,end = " ")


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math




def main():
    
    T=int(input())
    
    while(T>0):
        
        
        N=int(input())
        
        ob=Solution()
        
        ob.printNos(N)
        print()
        T-=1

if __name__=="__main__":
    main()
# } Driver Code Ends