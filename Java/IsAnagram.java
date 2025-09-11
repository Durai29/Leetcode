public class IsAnagram {
    public static boolean isAnagram(String s, String t) {
        if (s.length() != t.length()) return false; 
        int[] frequency = new int[26];
        // Arrays.fill(frequency, 0);   // No need to Arrays.fill(frequency, 0) → Java already initializes new arrays with 0.
        // char[] new_s = s.toCharArray(); //
        // char[] new_t = t.toCharArray();
        for(int i=0; i < s.length(); i++){
            // int temp_1 = ((int) new_s[i]-97);
            // frequency[temp_1] += 1;
            // int temp_2 = ((int) new_t[i]-97);
            // frequency[temp_2] -= 1;
            frequency[s.charAt(i) - (int)'a'] ++;
            frequency[t.charAt(i) - (int)'a'] --;
        }
        
        for(int i : frequency){
            if(i != 0) return false;
        }
        return true;
    }
    public static void main(String arg[]){
        System.out.println(isAnagram("anagram", "nagaram"));
        // isAnagram("live", "evil");
    }
}
