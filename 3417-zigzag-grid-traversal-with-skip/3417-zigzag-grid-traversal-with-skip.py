class Solution:
    def zigzagTraversal(self, grid):
        rows = len(grid)
        cols = len(grid[0])

        result = []
        count = 0

        for r in range(rows):

            if r % 2 == 0:
                columns = range(cols)
            else:
                columns = range(cols - 1, -1, -1)

            for c in columns:

                # Take every alternate cell
                if count % 2 == 0:
                    result.append(grid[r][c])

                count += 1

        return result