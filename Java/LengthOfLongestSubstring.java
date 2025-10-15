import java.util.HashMap;
import java.util.Map;

public class LengthOfLongestSubstring {
    public int lengthOfLongestSubstring(String s) {
        char[] s_char = s.toCharArray();
        int count = 0;
        Map<Character,Integer> pair = new HashMap<>();
        int left = 0;
        for(int right = 0; right < s.length(); right++){
            char c = s_char[right];
            if(pair.containsKey(c)){
                left = Math.max(left, pair.get(c)+1);
            }
            pair.put(c,right);
            count = Math.max(count, right-left+1);
        }
        return count;
    }
}

