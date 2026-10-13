class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        curr_max = -1
        n = len(arr) - 1
        for num in arr[::-1]:
            arr[n] = curr_max
            curr_max = max(curr_max, num)
            n -= 1
        return arr