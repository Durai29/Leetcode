public class SumOfDigits {
    public int getLucky(String s, int k) {
        int x = 0;
        int rem = 0;
        int res = 0;
        for(char ch : s.toCharArray()){
            x = (ch - 'a' + 1);
            while(x!=0){
                rem = x % 10;
                res += rem;
                x /= 10;
            }
        }
        x = res;
        res = 0;
    
        rem = 0;
        for(;(k-1)!=0;k--){
            while(x!=0){
                rem = x % 10;
                res += rem;
                x /= 10;
            }
            x = res;
            res=0;
        }
        return x;
    }
}