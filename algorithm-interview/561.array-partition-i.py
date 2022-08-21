# leetcode : 561.array-partition-i

from typing import List


# 풀이 1 (나의 풀이) : 오름차순 풀이
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        min_sum = 0
        pair = []
        nums.sort()

        for n in nums:
            pair.append(n)
            if len(pair) == 2:
                min_sum += min(pair)
                pair = []
        return min_sum


# 풀이 2 : 짝수 번째 값 계산
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        min_sum = 0
        nums.sort()

        for i, n in enumerate(nums):
            if i % 2 == 0:
                min_sum += n

        return min_sum


# 풀이 3 : 파이썬다운 방식
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        return sum(sorted(nums)[::2])
