class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_len, curr_len = 0,0
        n = len(nums)

        for i in range(len(nums)):
            if nums[i]==1:
                curr_len += 1
            else :
                curr_len = 0
            max_len = max(max_len, curr_len)
        return max_len    

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna