# 자연수 n을 뒤집어 각 자리 숫자를 원소로 가지는 배열 형태로 리턴해주세요. 예를들어 n이 12345이면 [5,4,3,2,1]을 리턴합니다.

# 첫번째 방법 : 실패
def solution(n):
    array = list(str(n))
    array.reverse()
    return array


# 두번째 방법 : map 이용
def solution(n):
    # 정수 상태로 배열 만들기 위한 방법
    array = list(map(int, str(n)))
    array.reverse()
    return array


# Refactor
def solution(n):
    return list(map(int, reversed(str(n))))
