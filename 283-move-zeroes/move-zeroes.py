class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        curr = 0
        next = 1
        while next <= len(nums)-1:
            if nums[curr] == 0:
                if nums[next]== 0:
                    next = next + 1
                else:
                    temp = nums[next]
                    nums[next] = nums[curr]
                    nums[curr] = temp
                    next = next + 1
                    curr = curr + 1
            else:
                next = next + 1
                curr = curr + 1
        