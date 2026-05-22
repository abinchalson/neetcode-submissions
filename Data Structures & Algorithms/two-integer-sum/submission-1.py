class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index_map = {}
        for index, num in enumerate(nums):
            index_map[num] = index
        for i, num in enumerate(nums):
            complement = target - num
            if complement in index_map and index_map[complement] != i:
                indices = [i, index_map[complement]]
                indices.sort()
                return indices
        return []