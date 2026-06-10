class Solution:
    def climbStairs(self, n: int) -> int:
        [0, 1, 1, 2, 3, 5, 8, 13]
        fib = [0, 1]
        for i in range(n):
            fib.append(fib[-1] + fib[-2])
        return fib[-1]