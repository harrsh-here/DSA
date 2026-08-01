class Solution:
    def mergeSort(self, arr, l, r):
        # code here
        if len(arr)<=1:
            return arr
        n = len(arr)
        mid = n//2
        left_arr = arr[:mid]
        right_arr = arr[mid:]
        
        left = self.mergeSort(left_arr,l,mid)
        right = self.mergeSort(right_arr,mid,r)
        sorted_arr = self.merge(left, right)

        for i in range(len(sorted_arr)):
            arr[i] = sorted_arr[i]
        
        return arr
        
        
    def merge(self,left,right):
        result = []
        i,j = 0,0
        n,m = len(left), len(right)
        
        while i<n and j<m:
            if left[i]<=right[j]:
                result.append(left[i])
                i+=1
            else : 
                result.append(right[j])
                j+=1
        if i<n:
            while i<n :
                result.append(left[i])
                i+=1
        if j<m:
            while j<m:
                result.append(right[j])
                j+=1
        return result
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna