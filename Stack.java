/**
 * @author Rohith Prabakar
 */
public class Stack {
	/**
	 * This class stack is my implementation of a stack.
	 * Stack is LIFO data structure.
	 * This is an array implementation of a stack of numbers.
	 */
	private int[] nums;
	private int top;   // denotes the top of the stack
	private boolean empty;
	/**
	 * Constructor to initialize values.
	 */
	
	public Stack() {
		nums = new int[10];
		top = 0;
		empty = true;
	}
	/**
	 * Adds number to the stack
	 * @param num: The number that is to be pushed.
	 */
	public void push(int num) {
		if(empty)
		{
			nums[0] = num;
			empty = false;
		}
		else {
			top++;
			if(top <= nums.length) // doesn't do anything \
				// if stack is filled
				nums[top] = num;
		}
	}
	/**
	 * Removes the top most element in stack
	 */
	public void pop() {
		if(top > 0)
			top--;
		else {
			empty = true;
		}
	}
	/**
	 * @return: The topmost element of the stack
	 */
	public int peek() {
		int result = -1;
		if(!empty)
			result = nums[top];
		return result;
	}
}
