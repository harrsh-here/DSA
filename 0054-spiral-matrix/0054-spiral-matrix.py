class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        m = len(matrix)
        n = len(matrix[0])
        top = 0
        bottom = m-1
        left = 0
        right = n-1
        res = []
        i,j = 0,0

        while left<= right and top <= bottom:
            # Top
            for j in range(left, right+1):
                res.append(matrix[top][j])
            top+=1
            
            # Right
            for i in range(top, bottom+1):
                res.append(matrix[i][right])
            right-=1
            
            if top<= bottom:
                # Bottom
                for j in range(right, left-1, -1):
                    res.append(matrix[bottom][j])
                bottom -=1
            
                # Left
                if left <= right:
                    for i in range(bottom, top-1, -1):
                        res.append(matrix[i][left])
                    left+=1
        return res

        
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna