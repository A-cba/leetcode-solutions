
leetcode 27：移除元素
题目：https://leetcode.cn/problems/remove-element/
解题思路：
  1. 定义快慢指针 fast=0, slow=0
  2. fast 每次走一步，扫描整个数组
  3. 如果 nums[fast] != val → 这个值要保留 → 复制到 nums[slow] → slow+=1
  4. 如果 nums[fast] == val → 跳过不要 → slow 不动
  5. 遍历结束，slow 就是新数组的长度
  6. 注意：题目不要求删除后面的元素，只要求前 slow 个正确
时间复杂度：O(n)
空间复杂度：O(1)
日期：2026-06-14
"""

class Solution:
    def removeElement(self, nums, val):
        fast = 0
        slow = 0
        size = len(nums)
        while fast < size:
            if nums[fast] != val:
                nums[slow] = nums[fast]
                slow += 1
            fast += 1
        return slow
