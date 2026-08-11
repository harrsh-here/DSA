class Solution {
    public int maxSubArray(int[] nums) {
       int total = 0 ;
       int max = Integer.MIN_VALUE;
        
       int n = nums.length;
       for(int i = 0; i<n; i++){
        total += nums[i];
        if (total>max){
        max = total;
        }
        if (total <0) {
            total = 0;
        }
       }
       return max;
    }
}

// Synced seamlessly with LeetHub Pro
// Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
// Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna