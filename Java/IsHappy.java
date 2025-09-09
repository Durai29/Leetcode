import java.util.*;

public class IsHappy {
    public static boolean isHappy(int n) {
        Set<Integer> set = new HashSet<>();
        int rem = 0;
        int sum = 0;
        while(n != 1){
            if(set.contains(n)) return false;
            set.add(n);
            while(n != 0){
                rem = n % 10;
                sum += (int) Math.pow(rem, 2);
                n /= 10;
            }
            n = sum;
            sum = 0;
        }
        return true;
    }

    public static void main(String arg[]){
        Scanner scn = new Scanner(System.in);
        System.out.print("Enter: ");
        int n = scn.nextInt();
        // int n = 7;
        System.out.println(isHappy(n));
        scn.close();
    }
}
