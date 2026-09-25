class Solution:
    def divide(self, dividend: int, divisor: int) -> int:

        # 32-bit integer limits
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        # Special overflow case
        if dividend == INT_MIN and divisor == -1:
            return INT_MAX

        # Determine the sign
        negative = (dividend < 0) != (divisor < 0)

        # Work with positive numbers
        dividend = abs(dividend)
        divisor = abs(divisor)

        quotient = 0

        while dividend >= divisor:

            value = divisor
            multiple = 1

            # Keep doubling while it still fits
            while value + value <= dividend:
                value += value
                multiple += multiple

            # Subtract the largest possible chunk
            dividend -= value
            quotient += multiple

        # Apply the sign
        if negative:
            quotient = -quotient

        # Keep result inside 32-bit range
        if quotient < INT_MIN:
            return INT_MIN
        if quotient > INT_MAX:
            return INT_MAX

        return quotient