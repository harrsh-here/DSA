class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        n = len(nums)
        
        low, high = 0, n-1
        lb, ub = -1,n
        lb_found = False

        while low<=high:
            mid = (low+high)//2
        
            if nums[mid]==target :
                lb = mid
                high = mid -1
                
            elif nums[mid] > target :
                
                high = mid - 1
            else:
                low = mid+1
        
        low, high = 0, n-1

        while low<=high:
            mid = (low+high)//2
            if nums[mid] > target :
                ub = mid
                high = mid - 1
            else:
                low = mid+1


        if lb == -1:
            return[-1,-1]

        return [lb,ub-1] 
                


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna