class Solution:
    def findFloor(self, arr, x):
        # code here
            n = len(arr)
            left, right = 0, n - 1
            lb = -1
            while left <= right:
                mid = left + (right - left) // 2
                if arr[mid] <= x:
                    lb = mid
                    left = mid + 1
                else :
                    right = mid - 1

            return lb

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna