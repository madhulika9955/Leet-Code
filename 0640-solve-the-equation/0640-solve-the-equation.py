class Solution:
    def solveEquation(self, equation: str) -> str:

        def parse(side):
            x_count = 0
            constant = 0

            # Make every '-' behave like '+ -'
            terms = side.replace("-", "+-").split("+")

            for term in terms:
                if not term:
                    continue

                if "x" in term:
                    coefficient = term.replace("x", "")

                    if coefficient == "" or coefficient == "+":
                        coefficient = 1
                    elif coefficient == "-":
                        coefficient = -1
                    else:
                        coefficient = int(coefficient)

                    x_count += coefficient

                else:
                    constant += int(term)

            return x_count, constant

        left, right = equation.split("=")

        left_x, left_num = parse(left)
        right_x, right_num = parse(right)

        # (left_x - right_x)x = right_num - left_num
        x_coefficient = left_x - right_x
        constant = right_num - left_num

        # No x remains
        if x_coefficient == 0:
            if constant == 0:
                return "Infinite solutions"
            else:
                return "No solution"

        answer = constant // x_coefficient

        return "x=" + str(answer)