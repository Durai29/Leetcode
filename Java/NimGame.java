public class NimGame {
    public boolean canWinNim(int n) {
        if(n < 4) return true;
        else if(n % 4 == 0){
            return false;
        }
        else{
            return true;
        }
    }
}
// Revised Today (16 OCT 2025)