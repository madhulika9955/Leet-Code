class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        candidates.sort()
        result = []

        def backtrack(start, target, path):
            # Target achieved
            if target == 0:
                result.append(path[:])
                return

            # Target exceeded
            if target < 0:
                return

            for i in range(start, len(candidates)):

                # Skip duplicate choices at the same level
                if i > start and candidates[i] == candidates[i - 1]:
                    continue

                # Since array is sorted
                # no later number can work either
                if candidates[i] > target:
                    break

                # Choose
                path.append(candidates[i])

                # Move to i + 1 because each element
                # can be used only once
                backtrack(i + 1, target - candidates[i], path)

                # Undo choice
                path.pop()

        backtrack(0, target, [])
        return result