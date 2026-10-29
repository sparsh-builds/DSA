import java.util.Scanner;

public class switchcaseday20 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter 1 for circle area and 2 for rctangle's");
        int n = sc.nextInt();
        int[] arr={1,2};
        System.out.println(Switch(n, arr));
        sc.close();
    }
    public static double Switch(int n ,int[] arr){
        int r= arr[0];
        int l=arr[0];
        int b=arr[1];
        double result=0;
        switch (n) {
            case 1:
                 result=Math.PI*r*r;
                
            case 2:
                result=l*b;
        
            default:
                break;
        }
        
                return result;

    }

}
