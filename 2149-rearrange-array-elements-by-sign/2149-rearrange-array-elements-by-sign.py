class Solution(object):
    def rearrangeArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        n = len(nums)
        pos = []
        neg = []
        
        for i in range(n):
            if nums[i]<0:
                neg.append(nums[i])
            else:
                pos.append(nums[i])

        i=0
        while i<len(pos):
            nums[i*2] = pos[i]
            nums[(i*2)+1] = neg[i]
            i+=1
            
        return nums

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna