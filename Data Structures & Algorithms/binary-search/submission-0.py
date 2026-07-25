class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            middle_index = (left + right) // 2
            middle_value = nums[middle_index]

            if middle_value == target:
                return middle_index
            elif middle_value < target:
                left = middle_index + 1
            else:
                right = middle_index - 1
        
        return -1