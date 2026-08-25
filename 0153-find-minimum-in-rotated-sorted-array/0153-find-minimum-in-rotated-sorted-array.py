class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        low = 0
        high = n - 1
        minimum = float('inf')
        if nums[low] <= nums[high]:
            minimum = min(minimum, nums[low])
            return minimum
        while low <= high:
            mid = (low + high) // 2
            print("low : ", low, "mid : ", mid, "High ", high)
            minimum = min(minimum, nums[mid])

            if nums[low] <= nums[mid]:

                minimum = min(minimum, nums[low])
                low = mid + 1


            else:
                high = mid - 1
        return minimum


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna