class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total = 0
        maxx = float('-inf')
        n = len(nums)
        for i in range(n):
            total += nums[i]
            maxx = max(maxx, total)
            if total<0:
                total = 0
        return maxx

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna