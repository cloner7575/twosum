from typing import List
import unittest


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        checked_nums = {}
        for index, num in enumerate(nums):
            complement = target - num
            if complement in checked_nums:
                return [checked_nums[complement], index]
            checked_nums[num] = index


class TestTwoSum(unittest.TestCase):

    def test_two_sum_case1(self):
        solution = Solution()
        self.assertEqual(solution.twoSum([2, 7, 11, 15], 9), [0, 1])

    def test_two_sum_case2(self):
        solution = Solution()
        self.assertEqual(solution.twoSum([3, 2, 4], 6), [1, 2])

    def test_two_sum_case3(self):
        solution = Solution()
        self.assertEqual(solution.twoSum([3, 3], 6), [0, 1])

    def test_two_sum_case4(self):
        solution = Solution()
        self.assertEqual(solution.twoSum([1, 5, 5, 2], 10), [1, 2])


if __name__ == '__main__':
    unittest.main()
