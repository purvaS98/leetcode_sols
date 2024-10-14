class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        left = 0
        right = len(letters) - 1
        res = letters[0]

        while(left <= right):
            mid = (left + right) // 2

            '''if letters[mid] > target and letters[mid] < res:
                res = letters[mid]
            elif letters[mid] < target:
                left = mid + 1
            elif letters[mid] > target:
                right = mid - 1
            
            while left <= right:
            mid = (left + right) // 2'''

            if letters[mid] > target:
                res = letters[mid]  # Update result if we find a greater letter
                right = mid - 1  # Search the left half
            else:
                left = mid + 1
        return res
        