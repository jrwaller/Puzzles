import java.util.Stack;

public class ReversePhrase {

	public static void reverse(String s)
	{
		Stack<Character> ws = new Stack<Character>();
		for (char c: s.toCharArray())
		{
			ws.push(c);
		}
		while (!ws.empty())
		{
			System.out.print(ws.pop());
		}
	}
}
