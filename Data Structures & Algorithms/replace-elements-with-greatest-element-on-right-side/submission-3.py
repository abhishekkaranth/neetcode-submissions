class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        curr_max = -1
        n = len(arr) - 1
        for num in arr[::-1]:
            arr[n] = curr_max
            curr_max = max(curr_max, num)
            n -= 1
        return arr
        # n = len(arr)
        # ans = [0] * n
        # rightMax = -1
        # for i in range(n - 1, -1, -1):
        #     ans[i] = rightMax
        #     rightMax = max(arr[i], rightMax)
        # return ans