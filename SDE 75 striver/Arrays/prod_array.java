import java.util.Arrays;

class prod_array{
    public static int[] productExceptSelf(int[] nums) {
       int[] ans = new int[nums.length] ;
        

        int prefix=1 ;

        int suffix=1;

        Arrays.fill(ans, 1); // Step 1: Initialize with 1s

        

        for (int i = 0; i < nums.length; i++) {
            // Update left side with prefix
            ans[i] *= prefix;
            prefix *= nums[i];

            // Update right side with suffix
            ans[nums.length - 1 - i] *= suffix;
            suffix *= nums[nums.length - 1 - i];
        }

        return ans;
    }
    public static void main(String[] args) {
        int[] nums = {1, 2, 3, 4};
        int[] result = productExceptSelf(nums);
        System.out.println(Arrays.toString(result)); // Output: [24, 12, 8, 6]
    }
}