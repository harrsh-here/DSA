class Solution:
    def findUnion(self, a, b):
        # code here 
        n= len(a)
        m = len(b)
        new = []
        i,j = 0,0
        
        while i<n and j<m:
            if a[i] <= b[j]:
                if len(new)==0 or new[-1] != a[i]:
                    new.append(a[i])
                    
                i+=1
            else:
                if len(new)==0 or new[-1] != b[j]:
                    new.append(b[j])
                    
                j+=1
            
            
        while i<n:
            if len(new)==0 or new[-1] != a[i]:
                new.append(a[i])
               
            i+=1
        while j<m:
            if len(new)==0 or new[-1] != b[j]:
                new.append(b[j])
                
            j+=1
        return new

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna