class Solution(object):
    def rearrangeArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        p,n = 0,1
        length = len(nums)
        res = [0] * length
        for i in range(length):
            if nums[i]<0:
                res[n] = nums[i]
                n+=2
            else:
                res[p] = nums[i]
                p+=2
        return res

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna