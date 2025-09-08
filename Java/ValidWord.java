// package Java;
import java.util.Set;
import java.util.HashSet;

// Leetcode : 3136
class Solution1 {
    public static boolean isValid(String word){
        if (word.length() < 3){
            return false;
        }

        Set<Character> vowels = new HashSet<>();
        for(char c : ("aeiou"+"AEIOU").toCharArray()) vowels.add(c);

        Set<Character> consonants = new HashSet<>();
        for(char c : (("bcdfghjklmnpqrstvwxyz"+"bcdfghjklmnpqrstvwxyz".toUpperCase()).toCharArray())) consonants.add(c);

        Set<Character> symbols = new HashSet<>();
        for(char c : ("@#$").toCharArray()) symbols.add(c);

        boolean v_flag = false;
        boolean c_flag = false;

        for (char c : word.toCharArray()){
            if (symbols.contains(c)){
                return false;
            }
            else if ((Character.isLetterOrDigit(c))){
                if (vowels.contains(c)){
                    v_flag = true;
                }
                else if (consonants.contains(c)){
                    c_flag = true;
                }
            }
        }

        return v_flag && c_flag;

    }
}

// Solution1 is mine Solution2 is an optimized solution

class Solution2 {
    // Define the vowel and symbol sets once
    private static final Set<Character> VOWELS = Set.of(
        'a', 'e', 'i', 'o', 'u',
        'A', 'E', 'I', 'O', 'U'
    );

    private static final Set<Character> SYMBOLS = Set.of('@', '#', '$');

    public static boolean isValid(String word) {
        if (word.length() < 3) return false;

        boolean hasVowel = false;
        boolean hasConsonant = false;

        for (char c : word.toCharArray()) {
            if (SYMBOLS.contains(c)) return false;

            if (Character.isLetter(c)) {
                if (VOWELS.contains(c)) {
                    hasVowel = true;
                } else {
                    hasConsonant = true;
                }
            } else if (!Character.isDigit(c)) {
                // Ignore digits, but if it's any other non-symbol character (like punctuation), return false
                return false;
            }
        }

        return hasVowel && hasConsonant;
    }
}


public class ValidWord {
    public static void main(String args[]){
        System.out.println(Solution2.isValid("234Adas"));
        System.out.println(Solution2.isValid("b3"));
        System.out.println(Solution2.isValid("a3$e"));
        System.out.println(Solution2.isValid("Ya$"));
    }
}