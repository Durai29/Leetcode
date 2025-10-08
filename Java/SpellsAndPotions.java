import java.util.Arrays;

public class SpellsAndPotions {
    public static int[] successfulPairs(int[] spells, int[] potions, long success) {
        int n = spells.length;
        int m = potions.length;
        int[] result = new int[n];
        Arrays.sort(potions);
        for(int i=0; i<n; i++){
            int left = 0;
            int right = m-1;
            int index = m;
            while(left <= right){
                int mid = left + (right - left) / 2;
                long target = (long) spells[i] * potions[mid];
                if(target >= success){
                    index = mid;
                    right = mid - 1;
                }else{
                    left = mid + 1;
                }
            }
            result[i] = m - index;
        }
        return result;
    }
}
