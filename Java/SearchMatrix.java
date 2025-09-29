public class SearchMatrix {
    public static boolean searchMatrix(int[][] matrix, int target) {
        int left = 0;
        int m = matrix.length;
        int n = matrix[0].length;
        int right = (m * n)-1;
        while(left <= right){
            int mid = (left + right) / 2;
            int x = mid / n;
            int y = mid % n;
            if(matrix[x][y]==target){ 
                return true;
            }else if(matrix[x][y]<=target) left = mid + 1;
            else right = mid - 1;
            // if(x < m && y < n){
            // }else break;
        }
        return false;
    }
}
