import java.util.*;

public class threesum {
    public static List<List<Integer>> method1(int[] arr ){
        Set<List<Integer>> st = new HashSet<>();

        // First loop for first element
        for (int i = 0; i < arr.length; i++) {
            // Second loop for second element
            for (int j = i + 1; j < arr.length; j++) {
                // Third loop for third element
                for (int k = j + 1; k < arr.length; k++) {
                    // If triplet sum is zero
                    if (arr[i] + arr[j] + arr[k] == 0) {
                        // Store sorted triplet to avoid duplicates
                        List<Integer> temp = Arrays.asList(arr[i], arr[j], arr[k]);
                        Collections.sort(temp);
                        st.add(temp);
                    }
                }
            }
        return new ArrayList<>(st);
    }
        return null;
}

    public static List<List<Integer>> method2(int[] arr) {

        Set <List<Integer>> st = new HashSet<>();

        for(int i =0;i<arr.length;i++){
            int left = i + 1, right = arr.length - 1;
            int target=-(arr[i]);

            

        while (left < right) {
            if (arr[left] + arr[right] == 0) {
                st.add(Arrays.asList(arr[i],arr[left], arr[right]));
            } else if (arr[left] + arr[right] < 0) {
                left++;
            } else {
                right--;
            }
        }
    }
        return new ArrayList<>(st);
    }
    
    public static void main(String[] args) {
        int arr[] = {-1,0,1,2,-1,-4};
        method1(arr);

        method2(arr);
    }
}
