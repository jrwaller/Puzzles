/*
 * Write a function that shifts all zero elements of an array to the end
 */
public class ZeroShift {

	public static void main(String[] args) {
		int[] arr = {2, 0, 5, 4, 2, 0, 1, 0, 3, 3, 0};
		shift(arr);
		print(arr);
		int[] zeroes = {0,0,0,0,0,0,0,0,0,0,0,0,1};
		shift(zeroes);
		print(zeroes);
		
	}
	
	public static void shift(int[] arr)
	{
		int start = 0;
		int end = arr.length - 1;
		while (start < end)
		{
			if (arr[start] == 0 && arr[end] != 0)
			{
				int temp = arr[end];
				arr[end] = arr[start];
				arr[start] = temp;
			}
			else if (arr[start] != 0 && arr[end] == 0)
			{
				start++;
			}
			else if (arr[start] == 0 && arr[end] == 0)
			{
				end--;
			}
			else
			{
				start++;
				end--;
			}
		}
	}
	
	public static void print(int[] arr)
	{
		for (int i = 0; i < arr.length; i++)
		{
			System.out.print(arr[i] + " ");
		}
		System.out.println();
	}
}
