class Solution:
    def isSorted(self, arr):

        n = len(arr)
        for i in range(0, n-2):
            if arr[i]> arr[i+1]:
                return False
        return True      # code here
            

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna