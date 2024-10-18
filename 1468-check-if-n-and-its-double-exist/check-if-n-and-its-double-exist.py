class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        res = set() 
        for num in arr:
            # Check if num*2 or num//2 (if even) exists in the set
            if num * 2 in res or (num % 2 == 0 and num // 2 in res):
                return True

            # Add the current number to the set
            res.add(num)

        return False