class Solution(object):
    def fib(self, num):     
        if num == 0 or num == 1 :
            return num
        return self.fib(num-1) + self.fib(num-2)
    
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna