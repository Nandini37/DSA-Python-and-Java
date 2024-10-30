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
