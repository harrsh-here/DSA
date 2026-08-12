class Solution(object):
    def rearrangeArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        n = len(nums)
        pos = []
        neg = []
        res = []
        for i in range(n):
            if nums[i]<0:
                neg.append(nums[i])
            else:
                pos.append(nums[i])

        i,j = 0,0
        while i<len(pos) or j<len(neg):
            res.append(pos[i])
            res.append(neg[j])
            i+=1
            j+=1
        return res

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna