import java.util.*;

public class ValidParentheses {
    public static boolean isValid(String s){
        Map<Character,Character> pair = new HashMap<>();
        Stack<Character> stack = new Stack<>();
        pair.put(')', '(');
        pair.put(']','[');
        pair.put('}','{');
        for(char ch : s.toCharArray()){
            if(!pair.containsKey(ch)){
                stack.push(ch);
            }
            else{
                if(stack.size() == 0 || stack.pop() != pair.get(ch)){
                    return false;
                }
            }
        }
        return stack.size()==0;
    }
    public static void main(String[] arg){
        System.out.println(isValid("()"));
    }
}
