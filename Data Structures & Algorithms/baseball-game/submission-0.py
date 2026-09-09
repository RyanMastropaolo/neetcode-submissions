class Solution:
    def calPoints(self, operations: List[str]) -> int:
        result = []
        for i in operations:
            if i == "+":
                add = result[-2] + result[-1]
                result.append(add)
            elif i == "C":
                result.pop()
            elif i == "D":
                double = result[-1] * 2
                result.append(double)
            else:
                result.append(int(i))
        return sum(result)