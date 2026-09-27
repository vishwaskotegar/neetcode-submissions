class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowSet = defaultdict(set)
        colSet = defaultdict(set)
        subSet = defaultdict(set)

        for r in range(9):
            for c in range(9):
                value = board[r][c]
                if value == ".":
                    continue
                if (value in rowSet[r]
                or value in colSet[c]
                or value in subSet[(r // 3, c // 3)]):
                    return False
                
                rowSet[r].add(value)
                colSet[c].add(value)
                subSet[(r // 3, c // 3)].add(value)

        return True