class Solution:
    def countFreq(self, arr, target):
        # code here
        n = len(arr)
        
        low, high = 0, n-1
        lb, ub = -1,n
        

        while low<=high:
            mid = (low+high)//2
        
            if arr[mid]==target :
                lb = mid
                high = mid -1
                
            elif arr[mid] > target :
                
                high = mid - 1
            else:
                low = mid+1
        
        low, high = 0, n-1

        while low<=high:
            mid = (low+high)//2
            if arr[mid] > target :
                ub = mid
                high = mid - 1
            else:
                low = mid+1


        if lb == -1:
            return 0

        return ub-lb
                

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna