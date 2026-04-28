class Solution {
    /**
     * @param {character[][]} board
     * @return {boolean}
     */
    isValidSudoku(board) {
        const seen = new Set();

        for (let i = 0; i < 9; ++i) {
            for (let j = 0; j < 9; ++j) {
                const num = board[i][j];

                if (num == ".") continue;
                
                const row_key = `${num} in row ${i}`;
                const col_key = `${num} in col ${j}`;
                const box_key = `${num} in box ${Math.floor(i/3)}-${Math.floor(j/3)}`;

                if (seen.has(row_key) || seen.has(col_key) || seen.has(box_key)) return false;

                seen.add(row_key);
                seen.add(col_key);
                seen.add(box_key);
            }
        }

        return true;
    }
}
