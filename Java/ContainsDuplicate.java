import java.util.*;

public class ContainsDuplicate {
    public static boolean containsDuplicate(int[] nums){
        Set<Integer> seen = new HashSet<>();
        for(int num : nums){
            if(seen.contains(num)){
                return true;
            }else{
                seen.add(num);
            }
        }
        return false;
    }
}

// Revised Today (28 SEP 2025)