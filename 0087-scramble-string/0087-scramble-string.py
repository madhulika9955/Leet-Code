class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:

        memo = {}

        def dfs(a, b):

            # Already the same
            if a == b:
                return True

            # Different letters -> impossible
            if sorted(a) != sorted(b):
                return False

            # Already calculated
            if (a, b) in memo:
                return memo[(a, b)]

            n = len(a)

            # Try every possible split
            for i in range(1, n):

                # Case 1: No swap
                if (dfs(a[:i], b[:i]) and
                    dfs(a[i:], b[i:])):

                    memo[(a, b)] = True
                    return True

                # Case 2: Swap
                if (dfs(a[:i], b[n-i:]) and
                    dfs(a[i:], b[:n-i])):

                    memo[(a, b)] = True
                    return True

            memo[(a, b)] = False
            return False

        return dfs(s1, s2)