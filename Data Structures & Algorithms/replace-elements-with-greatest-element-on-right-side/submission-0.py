class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        result = []
        for i in range(0, len(arr)):
            if i < len(arr) - 1:
                greatest = max(arr[i+1:])
                result.append(greatest)
            else:
                result.append(-1)
        return result
