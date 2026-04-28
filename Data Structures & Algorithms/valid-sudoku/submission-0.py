class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen = set()
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    continue

                num = board[i][j]

                row_key = f"{num} in row {i}"
                col_key = f"{num} in col {j}"
                box_key = f"{num} in box {i // 3}-{j // 3}"

                if row_key in seen or col_key in seen or box_key in seen:
                    return False

                seen.add(row_key)
                seen.add(col_key)
                seen.add(box_key)

        return True

                