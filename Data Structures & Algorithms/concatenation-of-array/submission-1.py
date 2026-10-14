class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        len_nums = len(nums)
        ans = [0] * (len_nums * 2)
        for i, num in enumerate(nums):
            ans[i] = ans[i+len_nums] = num

        return ans
        