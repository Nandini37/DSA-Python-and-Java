## Richie Rich - Codechef Solution
**Problem Statement**

Here is the problem statement: [CodeChef](
codechef.com/practice/course/1to2stars/LP1TO201/problems/CHFRICH)


### Approach

##### Mathematics Approach 
The approach to this problem is very easy.

Let's assume Codechef initial asset be A.
CodeChef want to increase his asset by X every year. Let n be the number of years. 
Thus, new asset = A+X*n

The new asset should be greater than or equal to B.
B>= A+X*n
Here we are considering minimum condition.

Thus, B= A+X*n

We are required to find the number of years.

Hence modified equation will be:
n = (B-A)/X

-----

#### Coding Approach

1) To take input cases number
2) To take input as array "100 200 10"
3) Split the array
4) Parse the array
5) Apply mathematical logic
6) Print the solution


-----
#### Java Solution
```
import java.util.*;
import java.lang.*;
import java.io.*;
import java.util.Scanner;

class Codechef
{
	public static void main (String[] args) throws java.lang.Exception
	{
		// your code goes here
	    Scanner scanner  = new Scanner(System.in);
	    
	    int t = scanner.nextInt();
	    scanner.nextLine();
	    
	    while (t > 0)
	    {
	        String s = scanner.nextLine();
	        String[] arr = s.split(" ");
	        
	        int A = Integer.parseInt(arr[0]);
	        int B = Integer.parseInt(arr[1]);
	        int X = Integer.parseInt(arr[2]);
	        
	        System.out.println((B-A)/X);
	        
	        t--;
	    }
	    
        scanner.close();
	}
}


```
----
#### Python solution

```
t = int(input())

while t > 0:
    s = input("")
    arr = s.split(" ")
    
    A = int(arr[0])
    B = int(arr[1])
    X = int(arr[2])
    
    print(int((B-A)/X))
    
    t = t-1!

```
----
