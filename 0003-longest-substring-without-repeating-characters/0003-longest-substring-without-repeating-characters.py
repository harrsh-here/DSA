class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s)<=1 :
            return len(s)
        
        left, right = 0,0
        #abcabc
        seen = set()
        s_max = 0
        for right in range(len(s)):
            # print("----")
            # print(s[right])
            # print(s[right] in seen)
            # print(left,right)
            while s[right] in seen:
                # print("Seen")
                seen.remove(s[left])
                left+=1
            new_max = right - left +1
            
                
            if s_max<new_max :
                s_max = new_max
            seen.add(s[right])
            # print(seen)
            # print(left,right)
            # print(s_max)
        return s_max       

        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna