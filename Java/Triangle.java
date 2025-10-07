import java.util.List;

public class Triangle {
    public int minimumTotal(List<List<Integer>> triangle) {
        if(triangle.isEmpty()) return 0;
        for(int i=triangle.size()-2; i>=0; i--){
            for(int j=0; j<triangle.get(i).size(); j++){
                int current = triangle.get(i).get(j);
                int a = triangle.get(i+1).get(j) + current;
                int b = triangle.get(i+1).get(j+1) + current;
                triangle.get(i).set(j,Math.min(a,b));
            }
        }
        return triangle.get(0).get(0);
    }
}
