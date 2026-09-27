class Solution:
    def combinationSum(self, candidates, target):

        result = []

        def backtrack(start, target, path):

            # We found a valid combination
            if target == 0:
                result.append(path[:])
                return

            # We went over the target
            if target < 0:
                return

            for i in range(start, len(candidates)):

                # Choose
                path.append(candidates[i])

                # Explore
                # i is passed again because we can reuse
                # the same number
                backtrack(i, target - candidates[i], path)

                # Undo
                path.pop()

        backtrack(0, target, [])

        return result