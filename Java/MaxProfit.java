class MaxProfit {                                       // Leetcode : 121
    public int maxProfit(int[] prices) {
        int min_price = Integer.MAX_VALUE;
        int max_price = 0;
        for(int p : prices){
            min_price = min_price < p ? min_price : p;
            int current_price = p - min_price;
            max_price = max_price > current_price ? max_price : current_price;
        }
        return max_price;
    }
}

// Revised Today (21 SEP 2025)