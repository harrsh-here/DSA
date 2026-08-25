class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n = len(nums)
        lb, ub = n,n
        low, high = 0,n-1

        while low <= high:
            mid = (low + high) // 2
            
            if nums[mid] == target :
                return mid
                
            elif nums[mid] > target:
                lb = mid
                high = mid - 1
            else :
                low = mid + 1

        return lb
            

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna