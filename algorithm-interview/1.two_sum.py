# leetcode : 1 Two Sum



class Solution(object):
    # 나의 풀이 : 브루트 포스 Runtime 4891ms
    def twoSum(self, nums, target):
        for i in range(0, len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

    # in을 이용한 탐색 (target - n이 존재하는지 확인) : Runtime 410ms
    def twoSum(self, nums, target):
        for i, n in enumerate(nums):
            complement = target - n

            if complement in nums[i + 1:]:
                return [nums.index(n), nums[i + 1:].index(complement) + (i + 1)]

    # 첫 번째 수를 뺀 결과 키 조회 : Runtime 48ms
    def twoSum(self, nums, target):
        nums_map = {}

        # 키와 값을 바꿔서 딕셔너리로 저장
        for i, num in enumerate(nums):
            nums_map[num] = i

        # 타켓에서 첫 번째 수를 뺀 결과를 키로 조회
        for i, num in enumerate(nums):
            if target - num in nums_map and i != nums_map[target - num]:
                return [i, nums_map[target - num]]

    # 조회 구조 개선 : Runtime 76ms
    def twoSum(self, nums, target):
        nums_map = {}
        # 하나의 `for`문으로 통합
        for i, num in enumerate(nums):
            if target - num in nums_map:
                return [nums_map[target - num], i]
            nums_map[num] = i

    # 투포인터 이용
    def twoSum(self, nums, target):
        left, right = 0, len(nums) - 1
        while not left == right:
            # 합이 타겟보다 크면 오른쪽 포인터를 왼쪽으로
            if nums[left] + nums[right] < target:
                left += 1
            # 합이 타겟보다 작으면 왼쪽 포인터를 오른쪽으로
            elif nums[left] + nums[right] > target:
                right -= 1
            else:
                return [left, right]
