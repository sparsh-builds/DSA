


import java.util.Scanner;



public class CheckifSortedDay18 {
    public static void main(String[] args) {
        int n;
        
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter Size of Array");
        n=sc.nextInt();
        int[] arr = new int[n];
        System.out.println("Enter Array Elements");
        for(int i=0;i<n;i++){
            arr[i]=sc.nextInt();
        }
        System.out.println(Sorted(arr,n));
        sc.close();

    }
    public static int Sorted(int[] a,int n){
        if(a[0]<a[n-1]){
            return 1;
        }
        return 0;
    }
}
