class Solution(object):
    def search(self, nums, target):

      # Trying Optimal Approach
        n = len(nums)
        low, high = 0, n-1

        while low<= high:
            mid = (low+high)//2
            #print(f"search : Low : {low}, mid : {mid}, high : {high}")
            if nums[mid] == target:
                return  mid
            if nums[low] <= nums[mid] and (nums[low] <= target <= nums[mid]) :
                 #print("first elif")
                 high = mid-1
            elif nums[low]<=nums[mid]:
                low = mid+1
            elif nums[high] >= nums[mid] and (nums[high] >= target >= nums[mid]) :
                #print("second elif")
                low = mid + 1
            elif nums[high] >= nums[mid] :
                high = mid - 1
        return -1

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna