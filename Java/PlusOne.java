public class PlusOne {
    public int[] plusOne(int[] digits) {
        int num = 1;
        for(int i = digits.length-1; i>=0; i--){
            digits[i] += num;
            num = digits[i] / 10;
            int rem = digits[i] % 10;
            if(num != 0){
                digits[i] = rem;
            }
            else break;
        }
        if(num != 0){
            int[] new_digits = new int[digits.length+1];
            new_digits[0] = num;
            for(int i=0; i<digits.length; i++){
                new_digits[i+1] = digits[i];
            }
            return new_digits;
        }
        return digits;
    }
}

// Revised Today (20 OCT 2025)