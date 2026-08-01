class Solution:
    def mergeSort(self, arr, l, r):
        # code here
        if l>=r:
            return
        n = l+r
        
        mid = n//2

        
        self.mergeSort(arr,l,mid)
        self.mergeSort(arr,mid+1,r)
        self.merge(arr, l,mid,r)
        return arr
        
        
    def merge(self,arr,l,mid,r):
        left = arr[l:mid+1]
        right = arr[mid+1:r+1]
        i,j,k = 0,0,l
        n,m = len(left), len(right)
        
        while i<n and j<m:
            if left[i]<=right[j]:
                arr[k] = left[i]
                i+=1
                k+=1
            else : 
                arr[k] = right[j]
                j+=1
                k+=1
        
        while i<n :
            arr[k] = left[i]
            i+=1
            k+=1
        
        while j<m:
            arr[k] = right[j]
            j+=1
            k+=1
        return 

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna