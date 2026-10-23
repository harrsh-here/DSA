class Solution:
    def countSetBits(self,n: int) -> int:
        # dp[i] will store the total set bits of number i
      
        n += 1
        count = 0
        
        # Store power of 2 (representing the length of the block of 1s)
        # 1 -> 2 -> 4 -> 8 ...
        power_of_2 = 1
        
        while power_of_2 < n:
           # Total size of a full cycle (0s followed by 1s)
           cycle_length = power_of_2 * 2
        
           # Number of complete cycles in the range
           full_cycles = n // cycle_length
           count += full_cycles * power_of_2
        
           # Check if there are remaining elements in the partial cycle
           remainder = n % cycle_length
           if remainder > power_of_2:
               count += remainder - power_of_2
        
           # Shift left to check the next bit position
           power_of_2 *= 2
        
        return count



# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna