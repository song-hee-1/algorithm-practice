# leetcode : 206 Reverse Linked List

from typing import List, Optional, List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# 재귀 구조로 뒤집기
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        def reverse(node: ListNode, prev: ListNode = None):
            if not node:
                return prev
            next, node.next = node.next, prev
            return reverse(next, node)

        return reverse(head)


# 반복 구조로 뒤집기
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        node, prev = head, None

        while node:
            next, node.next = node.next, prev
            prev, node = node, next

        return prev