

public class BinarySearchDay14 {

    public static void main(String[] args) {
        int n=16;
        int[] arr= {1,2,3,4,15,18};
        System.out.println(Binary(arr,n));
    }
    public static int Binary(int[] arr,int target){
        int size=arr.length;
        int l=0;
        int h=size-1;
        
        while (l<h) {
            int mid = l + (h-l)/2;
            if(arr[mid]==target){
                return 1;
            }
            else if(arr[mid]<target){
                l=mid+1;
            }
            else{
                h=mid-1;
                mid=l+(h-l)/2;

            }
        }
        return 0;
    }
}