public class ValidPalindrome {
    public static boolean isPalindrome(String s){
        // Stack<Character> stack = new Stack<>();
        // for(Character ch : s.toCharArray()){
        //     if(Character.isLetter(ch)){
        //         stack.push(Character.toLowerCase(ch));
        //     }            else if(Character.isDigit(ch)){
        //         stack.push(ch);
        //     }
        // }
        
        // Stack<Character> temp = new Stack<>();
        // temp.addAll(stack);
        // Stack<Character> reverse = new Stack<>();
        // while(!temp.empty()){
        //     reverse.push(temp.pop());
        // }
        // return stack.equals(reverse);
        int i = 0, j = s.length()-1;
        while(i<j){
            while(i<j && !Character.isLetterOrDigit(s.charAt(i))) i++;
            while(i<j && !Character.isLetterOrDigit(s.charAt(j))) j--;
            if(i<j){
                char left = Character.toLowerCase(s.charAt(i));
                char right = Character.toLowerCase(s.charAt(j));
                if(left != right) return false;
                i++; j--;
            }
        }
        return true;
    }

    public static void main(String arg[]){
        System.out.println(isPalindrome("0P"));
        System.out.println(isPalindrome("Madam"));
    }
}
