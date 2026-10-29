public class NumberofInversionsDay13 {
    public static void main(String[] args) {
        int[] arr={5,3,2,1,4};
        System.out.println(Inversions(arr));
    }
    public static int Inversions(int[] arr){
        int left=0;
        int right=arr.length-1;
        int count=0;
        int r = arr.length-1;
        int ans =Count(arr, left, right,count,r);

        
        return ans;
    }
    public static int Count(int[] arr,int left,int right,int count,int r){
        
        while(left<right){
            
            if(arr[left]>arr[r]){
                count++;
                r--;
            }
            else{
                left++;
                r=arr.length-1;
                Count(arr, left, right, count, r);
            }
    }
    return count;
}
}
