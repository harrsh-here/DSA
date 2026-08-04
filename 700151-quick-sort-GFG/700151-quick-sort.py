class Solution:
    def quickSort(self, arr, low, high):
        # code here 
        if low>high:
            return
        mid_index = self.partition(arr, low, high)
        self.quickSort(arr, low, mid_index-1)
        self.quickSort(arr,mid_index+1,high)
        

    def partition(self, arr, low, high):
        # code here
        i,j = low,high
        pivot = arr[low]
        
        while i<j:
            while arr[i]<=pivot and i<high :
                i+=1
                
            while arr[j]>=pivot and j > low:
                j-=1
            if i<j:
                arr[i],arr[j] = arr[j], arr[i]
                
        arr[low], arr[j] = arr[j], arr[low]
        return j

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna