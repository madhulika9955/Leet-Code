class Solution:
    def myAtoi(self, s: str) -> int:

        i = 0
        n = len(s)

        # 1. Skip leading spaces
        while i < n and s[i] == ' ':
            i += 1

        # 2. Check sign
        sign = 1

        if i < n and s[i] == '-':
            sign = -1
            i += 1

        elif i < n and s[i] == '+':
            i += 1

        # 3. Read digits
        num = 0

        while i < n and s[i].isdigit():

            num = num * 10 + int(s[i])

            # 4. Check overflow
            if sign == 1 and num > 2147483647:
                return 2147483647

            if sign == -1 and num > 2147483648:
                return -2147483648

            i += 1

        return sign * num