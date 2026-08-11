class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        j=0
        k = k%n
        if k==0:
            return
        def reverse(nums, l,r):
            while(l<r):
                nums[l],nums[r] = nums[r],nums[l]
                l+=1
                r-=1
        reverse(nums,n-k,n-1)
        reverse(nums,0, n-k-1)
        reverse(nums,0,n-1)
 
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna