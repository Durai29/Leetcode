import java.util.*;

public class RemoveAnagrams {
    public static List<String> removeAnagrams(String[] words){
        List<String> wordsList = new ArrayList<>(Arrays.asList(words));
        for(int i=1; i<wordsList.size(); i++){
            if(isAnagram(wordsList.get(i-1), wordsList.get(i))){
                wordsList.remove(i);
                i--;
            }
        }
        return wordsList;
        
    }
    private static boolean isAnagram(String s1, String s2){
        if(s1.length() != s2.length()) return false;
        char[] s1CharArray = s1.toCharArray();
        char[] s2CharArray = s2.toCharArray();
        Arrays.sort(s1CharArray); 
        Arrays.sort(s2CharArray);
        return Arrays.equals(s1CharArray, s2CharArray);
    }
    public static void main(String arg[]){
        System.out.println(removeAnagrams(new String[]{"abba", "baba", "bbaa", "cd", "cd"}));
    }
}
