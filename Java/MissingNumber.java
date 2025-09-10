public class MissingNumber {
    public int missingNumber(int[] nums) {
        int val = ((nums.length)*(nums.length + 1)) / 2;
        int sum = 0;
        for(int i = 0; i < nums.length; i++){
            sum += nums[i];
        }
        return val - sum;
    }
}
