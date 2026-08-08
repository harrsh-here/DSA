class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return 1
        i = 0
        j = i+1
        n = len(nums)

        while j<n:
            if nums[i] != nums[j]:
                i+=1
                nums[j], nums[i] = nums[i],nums[j]
            j+=1
        return i+1
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna