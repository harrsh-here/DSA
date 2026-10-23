class Solution:
    def divide(self, dividend, divisor):
        # 1. Handle 32-bit signed integer overflow cases
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        
        if dividend == INT_MIN and divisor == -1:
            return INT_MAX
        
        # 2. Determine the sign of the result
        # If one is negative and the other is positive, the result is negative
        negative = (dividend < 0) ^ (divisor < 0)
        
        # 3. Work with absolute (positive) values
        dividend = abs(dividend)
        divisor = abs(divisor)
        
        quotient = 0
        
        # 4. Exponential search / Bit manipulation loop
        while dividend >= divisor:
            temp_divisor = divisor
            multiple = 1
            
            # Double the divisor until it's bigger than the remaining dividend
            while dividend >= (temp_divisor << 1):
                temp_divisor <<= 1
                multiple <<= 1
            
            # Subtract the largest found multiple from dividend and add to quotient
            dividend -= temp_divisor
            quotient += multiple
            
        # 5. Apply the correct sign and clamp to 32-bit range
        if negative:
            quotient = -quotient
            
        return max(INT_MIN, min(INT_MAX, quotient))


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna