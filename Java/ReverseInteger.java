import java.util.*;

class ReverseInteger {
    public static int reverse(int num) {
        int rev=0, rem = 0;
        if (num < Integer.MIN_VALUE || num > Integer.MAX_VALUE) return 0;
        while(num != 0){
            rem = num % 10;
            rev = rev * 10 + rem;
            if (rev < Integer.MIN_VALUE || rev > Integer.MAX_VALUE) return 0;
            num/=10;
        }
        return rev;
    }

    public static void main(String arg[]){
        Scanner scn = new Scanner(System.in);
        System.out.print("Enter: ");
        // int n = scn.nextInt();
        int n = 1534236469;
        System.out.println(reverse(n));
        scn.close();
    }
}
