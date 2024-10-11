//Recursion Problem:

// Print 1 To N Without Loop


class Solution
{
    
  public void printNos(int N)
    {
        if (N<1)
        {
            return;
        }
        else 
        {
            printNos(N-1);
            System.out.print(N + " ");
        }
        
        
        }
    }


