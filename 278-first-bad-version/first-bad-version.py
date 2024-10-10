# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left = 0
        right = n - 1
        
        while(left <= right):
            mid = int(math.floor((left+right)/2))
            if isBadVersion(mid) == True:
                right = mid -1
            else:
                left = mid + 1
        return left
        