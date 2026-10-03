class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        remainder_dict = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in remainder_dict.keys():
                return [remainder_dict[diff], i]
            remainder_dict[num] = i
                