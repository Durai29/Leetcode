class MaxFruit {
    public int totalFruit(int[] fruits) {
         Map<Integer,Integer> frequency = new HashMap<>();
        int maxFruits = 0;
        int left = 0;
        for(int right=0; right<fruits.length; right ++){
            int fruit = fruits[right];
            frequency.put(fruit,frequency.getOrDefault(fruit,0)+1);
            while(frequency.size()>2){
                int leftFruit = fruits[left];
                frequency.put(leftFruit,frequency.get(leftFruit)-1);
                if(frequency.get(leftFruit)==0){
                    frequency.remove(leftFruit);
                }
                left++;
            }
        maxFruits = Math.max(maxFruits,(right-left+1));
        }
        return maxFruits;
    }
}
