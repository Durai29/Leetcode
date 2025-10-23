// Leetcode : 1518
public class NumWaterBottles {          
    public int numWaterBottles(int numBottles, int numExchange) {
        int total = numBottles;
        while(numBottles > 1){
            int remaining = numBottles % numExchange;
            numBottles = numBottles / numExchange;
            total += numBottles;
            numBottles = numBottles + remaining;
            if(numBottles < numExchange) break;
        }
        return total;
    }
}
// Revised Today (23 OCT 2025)