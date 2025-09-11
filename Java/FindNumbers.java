public class FindNumbers {
    public static int findNumbers(int[] nums) {
        int count=0;
        for(int num:nums){
            int temp = 0;
            while(num != 0){
                temp++;
                num /= 10;
            }
            if(temp % 2==0) count++;
        }
        return count;
    }
    public static void main(String arg[]){
        System.out.println(findNumbers(new int[]{12,345,2,6,7896}));
    }
}
