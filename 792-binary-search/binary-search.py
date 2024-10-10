class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) -1
        
        while(left <= right):
            mid = int(math.floor((left+right)/2))
            if target == nums[mid]:
                return mid
            elif nums[mid]  > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
        return -1
        
        
        