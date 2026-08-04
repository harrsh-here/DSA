class Solution:
    def countFactors (self, n):
        # code here
        num =n
        count = 0
        for i in range(1, int((num**0.5)+1)):
            
            if num%i == 0:
                count+=1
                
                if num//i != i:
                    count+=1
                    
        return count

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna