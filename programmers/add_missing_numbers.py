# 0부터 9까지의 숫자 중 일부가 들어있는 정수 배열 numbers가 매개변수로 주어집니다.
# numbers에서 찾을 수 없는 0부터 9까지의 숫자를 모두 찾아 더한 수를 return 하도록 solution 함수를 완성해주세요.

from collections import Counter

# Counter 이용하여 등장하지 않은 숫자를 합할까 => Counter 결과 0번 등장한 것은 나타나지 않음


# 나의 풀이 : for loop
def solution(numbers):
    answer = 0
    for i in range(10):
        if i not in numbers:
            answer += i
    return answer


# 다른 사람의 풀이 : list comprehension 이용
def solution(numbers):
    return sum([i for i in [1, 2, 3, 4, 5, 6, 7, 8, 9, 0] if i not in numbers])


# 다른 사람의 풀이 : lambda + sum 이용
solution = lambda x: sum(range(10)) - sum(x)
