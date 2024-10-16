class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
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
        