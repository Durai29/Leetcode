import java.util.*;

public class CreateTargetArray {
    public static int[] createTargetArray(int[] nums, int[] index) {
        // int[] result = new int[index.length];
        // for(int i=0; i<index.length; i++){
        //     result[index[i]] = nums[i];
        // }
        // return result;
        ArrayList<Integer> result = new ArrayList<>();
        for(int i=0; i<index.length; i++){
            result.add(index[i],nums[i]);
        }
        int res[] = new int[result.size()];
        for(int i=0; i < result.size(); i++){
            res[i] = result.get(i);
        }
        return res;
    }
    public static void main(String arg[]){
        int[] nums = new int[]{0,1,2,3,4};
        int[] index = new int[]{0,1,2,2,1};
        System.out.println(Arrays.toString(createTargetArray(nums, index)));
    }
}
