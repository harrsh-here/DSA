class Solution:
    def bubbleSort(self,arr):
        # code here
        n = len(arr)
        for i in range(n-2,-1,-1):
            is_swap = False
            for j in range(i+1):
                if arr[j]>arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
                    is_swap = True
            if is_swap==False:
                break
    

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna