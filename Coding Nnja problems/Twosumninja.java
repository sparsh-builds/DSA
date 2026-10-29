import java.util.HashSet;
import java.util.Set;

public class Twosumninja {
    public static void main(String[] args) {
        int[] arr = {1,2,3,4,5};
        System.out.println(TwoSum(arr,8));
        
    }
    public static String TwoSum(int[] arr,int target){
        Set<Integer> seen=new HashSet<>();
        for(int i=0;i<arr.length;i++){
            int complement=target-arr[i];
            if(seen.contains(complement)){
                return "Yes";
            }
            seen.add(arr[i]);
        }
        return "NO";
    }
}
