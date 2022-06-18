# 첫번째 시도 -> 테스트 2에서 실패
# 입력값 〉	[3, 30, 34, 5, 9]
# 기댓값 〉	"9534330"
# 실행 결과 〉	실행한 결괏값 "9534303"이 기댓값 "9534330"과 다릅니다.
def solution1(numbers):
    numbers_str = list(map(str, numbers))
    numbers_str.sort(reverse=True)
    return ''.join(numbers_str)

# 두번째 시도 ->  테스트 11에서 실패
# 실행한 결괏값 "9534303"이 기댓값 "9534330"과 다른 이유는 30과 3의 순서 때문이므로 이를 해결하기 위해 * 3을 해줌
# (numbers의 원소는 1000이하인 조건 때문)
def solution2(numbers):
    numbers_str = list(map(str, numbers))
    numbers_str.sort(key=lambda x : x * 3, reverse=True)
    return ''.join(numbers_str)

# 세번째 시도 -> 통과
# 테스트 케이스에 "0000"이 존재할 때 생기는 오류를 방지하기 위해 "0000"을 "0"으로 바꾸기 위해 최종값에 str(int)형 변환을 해줘야 함
def solution3(numbers):
    numbers_str = list(map(str, numbers))
    numbers_str.sort(key=lambda x : x * 3, reverse=True)
    answer = ''.join(numbers_str)
    return str(int(answer))