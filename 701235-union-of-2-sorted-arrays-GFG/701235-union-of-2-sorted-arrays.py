class Solution:
    def findUnion(self, a, b):
        # code here 
        n= len(a)
        m = len(b)
        new = []
        i,j = 0,0
        last_element = None
        while i<n and j<m:
            if a[i] <= b[j]:
                if last_element != a[i]:
                    new.append(a[i])
                    last_element = a[i]
                i+=1
            else:
                if last_element != b[j]:
                    new.append(b[j])
                    last_element = b[j]
                j+=1
            
            
        while i<n:
            if last_element != a[i]:
                new.append(a[i])
                last_element = a[i]
            i+=1
        while j<m:
            if last_element != b[j]:
                new.append(b[j])
                last_element = b[j]
            j+=1
        return new

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna