class Solution:
    def generate(self, numRows: int) -> List[List[int]]:

        result = []
        
        for line in range(1, numRows + 1): 
            row = []
            C = 1  # used to represent C(line, i)
            for i in range(1, line + 1):
                row.append(C)  # Append the current value of C to the row
                C = int(C * (line - i) / i)  # Update C to the next value in the row
            result.append(row)  # Append the row to the result list
        
        return result  