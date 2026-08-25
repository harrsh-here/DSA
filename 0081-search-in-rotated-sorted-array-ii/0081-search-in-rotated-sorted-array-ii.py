class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool

        T.C. -> avg -> O(logN) | worst -> O(N/2)
        S.C. -> O(1)
        """
        n = len(nums)
        low = 0
        high = n-1

        while low <= high:
            mid = (low+high)//2
            # print("low : ", low, "mid : ", mid, "High ", high)
            if nums[mid] == target:
                return True
            if nums[low] == nums[mid] == nums[high]:
                low +=1
                high -=1
                continue

            if nums[low] <= nums[mid]:

                if nums[low] <= target < nums[mid]:
                    high = mid - 1

                else:
                    low = mid + 1
            else:
                if nums[high] >= target > nums[mid]:
                    low = mid + 1
                else:
                    high = mid - 1
        return False




# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna