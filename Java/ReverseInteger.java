class Solution {
    public int reverse(int x) {
        int rev = 0;
        boolean flag = false;
        if(x < 0){
            x *= -1;
            flag = true;
        }
        while(x != 0){
            int temp = x % 10;
            if(rev < Integer.MIN_VALUE/10 || (rev < Integer.MIN_VALUE/10 && temp < -8)) return 0;
            if(rev > Integer.MAX_VALUE/10 || (rev > Integer.MAX_VALUE/10 && temp > 7)) return 0;
            rev = rev * 10 + temp;
            x /= 10;
        }
        if(flag) rev *= -1;
        return rev;
    }
}