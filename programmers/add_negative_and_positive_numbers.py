# 어떤 정수들이 있습니다.
# 이 정수들의 절댓값을 차례대로 담은 정수 배열 absolutes와 이 정수들의 부호를 차례대로 담은 불리언 배열 signs가 매개변수로 주어집니다.
# 실제 정수들의 합을 구하여 return 하도록 solution 함수를 완성해주세요.
#
# 입출력 예
# absolutes	    signs	       result
# [4,7,12]	[true,false,true]	9
# [1,2,3]	[false,false,true]	0


# 나의 풀이 : zip 이용
def solution(absolutes, signs):
    answer = 0
    for value, sign in zip(absolutes, signs):
        if sign:
            answer += value
        else:
            answer -= value
    return answer


# 다른 사람의 풀이 : zip + sum 이용
def solution(absolutes, signs):
    return sum(absolutes if sign else -absolutes for absolutes, sign in zip(absolutes, signs))
