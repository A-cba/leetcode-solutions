"""
LeetCode 704: 二分查找
题目：https://leetcode.cn/problems/binary-search/
作者：常博奥
解题思路：
  1. 定义左右指针 left=0, right=len(nums)-1
  2. 每次取中间位置 mid = left + (right-left)//2（避免溢出）
  3. nums[mid] == target → 找到了，返回 mid
  4. nums[mid] < target → target 在右边，left = mid + 1
  5. nums[mid] > target → target 在左边，right = mid - 1
  6. 循环结束没找到 → 返回 -1
时间复杂度：O(log n)
空间复杂度：O(1)
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
