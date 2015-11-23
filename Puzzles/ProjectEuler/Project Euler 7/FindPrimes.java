/*
 * What is the 10 001st prime number?
 */
public class FindPrimes {

	public static void main(String[] args) {
		int numberOfPrimes = 0;
		int startNum = 2;
		while (numberOfPrimes != 10001)
		{
			if (isPrime(startNum))
			{
				numberOfPrimes++;
				System.out.println(startNum + " is prime");
			}
			startNum++;
		}

	}
	
	public static boolean isPrime(int n)
	{
		for (int i = 2; i <= Math.sqrt(n); i++)
		{
			if (n % i == 0)
			{
				return false;
			}
		}
		return true;
	}

}
