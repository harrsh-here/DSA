class Solution: 
    def selectionSort(self, arr):
        # code here
        n = len(arr)
        for i in range(n-1):
            min_index = i
            for j in range(i+1,n):
                if arr[j]<arr[min_index]:
                    min_index = j
            arr[i], arr[min_index] = arr[min_index], arr[i]
        return arr

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna