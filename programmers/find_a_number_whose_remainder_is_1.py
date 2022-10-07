# 자연수 n이 매개변수로 주어집니다. n을 x로 나눈 나머지가 1이 되도록 하는 가장 작은 자연수 x를 return 하도록 solution 함수를 완성해주세요.


# 내 풀이
def solution(n):
    for i in range(1, n):
        if n % i == 1:
            return i


# 가장 많은 좋아요를 받은 풀이 : list comprehension 이용(22.10.7기준)
def solution(n):
    return [x for x in range(1, n+1) if n % x == 1][0]
