import java.util.*;

public class TwoSum {                                                       // Leetcode : 1
    public static int[] twoSum(int[] nums, int target){                     // twoSum method definition
        Map<Integer,Integer> map = new HashMap<>();                         // used HashMap interface to store key : values pairs of num and it's index.
        for(int i=0; i < nums.length; i++){                                 // used a for loop to iterate the given array
            int complement = target - nums[i];                              // find the complement or the number that we need to find in the array.
            if(map.containsKey(complement)){                                // check if the complement is present inside the hashmap
                return new int[]{i,map.get(complement)};                    // if so return both the indices
            }
            map.put(nums[i], i);                                            // add the number and it's index to the hashmap
        }
        return new int[]{};                                                 // if the pairs or not found return empty array object.
    }

    public static void main(String args[]){
        int[] nums = {2,7,11,15};
        int target = 9;
        int[] result = twoSum(nums, target);
        System.out.println("Indices: " + result[0] + ", " + result[1]);
    }
}

// Revised Today (25 SEP 2025)