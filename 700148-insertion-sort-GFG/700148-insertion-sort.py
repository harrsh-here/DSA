class Solution:
    def insertionSort(self, arr):
        # code here
        n = len(arr)
        for i in range(1,n):
            if(arr[i]<arr[i-1]):
                key = arr[i]
                for j in range(i-1,-2,-1):
                    if(arr[j]<key) or j<0:
                        arr[j+1] = key
                        break
                    else :
                        arr[j+1] = arr[j]

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna