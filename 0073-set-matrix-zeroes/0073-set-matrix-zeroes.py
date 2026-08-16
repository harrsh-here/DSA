class Solution(object):
    def setZeroes(self, matrix):
        r = len(matrix)
        c = len(matrix[0])

        for i in range(r):
            for j in range(c):
                if matrix[i][j] == 0:
                    
                    for k in range(c):
                        if matrix[i][k]:
                            matrix[i][k]= float('inf')
                    for k in range(r):
                        if matrix[k][j]:
                            matrix[k][j] = float('inf') 
        for i in range(r):
            for j in range(c):
                if matrix[i][j] == float('inf'):
                    matrix[i][j] = 0 
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna