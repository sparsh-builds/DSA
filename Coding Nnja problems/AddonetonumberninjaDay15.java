
import java.util.*;

public class AddonetonumberninjaDay15 {
    public static void main(String[] args) {
         ArrayList<Integer> arr = new ArrayList<>(Arrays.asList(0,1,2,3,9));
         ArrayList<Integer> result= new ArrayList<>(Addonetonumbber(arr));
         System.out.println(result);
    }
    public static ArrayList<Integer> Addonetonumbber(ArrayList<Integer> arr){
        int n =arr.size();

        int carry=1;
        
        for(int i=n-1;i>=0;i--){
            int sum = arr.get(i) + carry;
            if(sum>=10){
                arr.set(i, sum%10);
                carry=sum/10;
            }
            else{
                arr.set(i,sum);
                carry=0;
                break;
            }
        }
        if(carry!=0){
            arr.add(0,carry);
        }
        while (arr.size()>1 & arr.get(0)==0) {
            arr.remove(0);
        }
        return arr;
    }
}
