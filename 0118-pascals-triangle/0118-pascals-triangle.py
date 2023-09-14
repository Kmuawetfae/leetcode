class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = []
        per_row = []
        
        for i in range(numRows):
            if i + 1 == 1 or i + 1 == 2:
                per_row.append(1)
            else:

                new_list = []
                for j in range(len(per_row) - 1):
                    new_list.append(per_row[j] + per_row[j + 1])
                per_row = new_list
                
                per_row.append(1)
                per_row.insert(0,1)

            
            result.append(per_row.copy())
        return result

