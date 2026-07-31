class Solution:
    def fib(self, n):
        memo = {}

        def solve(x):
            if x in memo:
                return memo[x]

            if x <= 1:
                return x

            memo[x] = solve(x-1) + solve(x-2)
            return memo[x]

        return solve(n)

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna