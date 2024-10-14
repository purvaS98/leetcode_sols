class Solution:
    def arrangeCoins(self, n: int) -> int:
        sum = 0 
        i = 1

        if n == 1:
            return 1

        while sum < n:
            sum += i
            i += 1
        
        if sum == n:
            return i-1
        else:
            return i-2
        