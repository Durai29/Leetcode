public class PowerOfTwo {                           // Leetcode : 231
    public static boolean isPowerOfTwo(int n){
        return (n & (n-1)) == 0;
    }
}
