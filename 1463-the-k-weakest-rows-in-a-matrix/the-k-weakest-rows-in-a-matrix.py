class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        
        ''' Approach 1 : Using 2 loops
        res = []
        
        for i in range(len(mat)):
            rowcount = 0
            for j in range(len(mat[i])):
                if mat[i][j] == 1:
                    rowcount += 1
                
            res.append((rowcount, i))
        
        res.sort()

        # Extract the first 'k' indices of the weakest rows
        return [index for _, index in res[:k]]
        '''

        res = []

        # Iterate over each row with its index
        for i, row in enumerate(mat):
            rowcount = sum(row)  # Count the number of 1s in the current row
            res.append((rowcount, i))  # Store (count of 1s, row index)

        # Sort by the count of 1s, and in case of a tie, by the row index
        res.sort()

        # Extract the first 'k' indices of the weakest rows
        return [index for _, index in res[:k]]