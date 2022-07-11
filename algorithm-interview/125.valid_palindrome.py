# leetcode : 125 Valid Palindrome

# 나의 풀이 : Runtime: 57ms, Memory Usage: 15.5MB
import re


class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = re.sub('[^a-zA-Z0-9]', '', s)
        reverse_s = s[::-1]
        if s == reverse_s:
            return True
        else:
            return False


# 풀이 1 : 리스트로 변환 Runtime: 304ms
class Solution:
    def isPalindrome(self, s: str) -> bool:
        strs = []
        for char in s:
            # isalnum : 영문자, 숫자 여부 판별 함수
            if char.isalnum():
                strs.append(char.lower())

        # 팰린드롬 여부 판별
        while len(strs) > 1:
            if strs.pop(0) != strs.pop():
                return False

        return True


# 풀이 2 : 데크 자료형을 이용한 최적화 Runtime: 64ms
import collections
from typing import Deque


class Solution:
    def isPalindrome(self, s: str) -> bool:
        # 자료형 데크로 선언
        strs: Deque = collections.deque()

        for char in s:
            if char.isalnum():
                strs.append(char.lower())

        while len(strs) > 1:
            if strs.popleft() != strs.pop():
                return False

        return True


# 풀이 3: 슬라이싱 사용 Runtime: 36ms
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        # 정규식으로 불필요한 문자 필터링
        s = re.sub('[^a-z0-9]', '', s)

        return s == s[::-1]  # 슬라이싱
