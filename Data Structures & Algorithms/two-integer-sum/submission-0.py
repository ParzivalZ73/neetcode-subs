class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map={}
        for i, v in enumerate(nums):
            complement = target - nums[i]
            if complement in map:
                return [map[complement], i]
            map[v] = i