class Solution:
    def largest(self, arr):
        # code here
        largest = arr[0]
        
        for i in range(len(arr)):
            largest = max(largest,arr[i])
        
        return largest


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna