# leetcode : 344 reverse string

# 나의 풀이
from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        s.reverse()


# 풀이 1 : 투 포인터를 이용한 스왑
class Solution:
    def reverseString(self, s: List[str]) -> None:
        left, right = 0, len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1


# 풀이 2 : 파이썬다운 방식
class Solution:
    def reverseString(self, s: List[str]) -> None:
        s.reverse()
