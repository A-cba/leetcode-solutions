"""
LeetCode 704: 二分查找
题目：https://leetcode.cn/problems/binary-search/
作者：常博奥
日期：2026-06-12
"""

class Solution:
    def search(self, nums: list[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1

# 测试
if __name__ == "__main__":
    s = Solution()
    print(s.search([-1, 0, 3, 5, 9, 12], 9))   # 输出 4
    print(s.search([-1, 0, 3, 5, 9, 12], 2))   # 输出 -1
    print(s.search([5], 5))                      # 输出 0
