public class Searchinrotatedsortedarray {
    public static int search(int[] nums, int target) {
    
        int left =0;
        int right=nums.length -1;
        while (left<=right){
            int mid =left+(right -left)/2;
            if(nums[mid]==target){
                return mid;
            }
            else {
                if(nums[mid]<target){
                    left++;

                }
                else{
                    right--;
                }
            }
        return -1;
    }

    public static void main(String[] args) {
       
        int arr[] = {4,5,6,7,0,1,2};
        int target = 0;
        System.out.println(search(arr, target));
    }
}
