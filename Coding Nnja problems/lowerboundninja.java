public class lowerboundninja {
    public static void main(String[] args) {
        int[] arr={1,2,2,3,4,5};
        System.out.println(lowerbound(arr, 6,7));
    }
    public static int lowerbound(int arr[],int n, int x){
        int low=0;
        int high=n-1;
        while(low<=high){
            int mid=low+(high-low)/2;
            if(arr[mid]>=x){
                high=mid-1;
            }
            else{
                low=mid+1;
            }
        }
        return low;
    }
}
