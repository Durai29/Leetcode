public class MaxBottlesDrunk {
    public int maxBottlesDrunk(int numBottles, int numExchange) {
        int drank = numBottles;
        while (numBottles > 1) {
            if(numBottles >= numExchange){
                numBottles -= numExchange;
                numBottles++;
                numExchange++;
                drank++;
            }
            else break;
        }
        return drank;
    }
}
