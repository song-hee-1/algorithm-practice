# 처음 풀이 : split() 이용하여 시간 초과
def solution(s):
    answer = ''
    words = s.split()
    for w in words:
        for i, v in enumerate(w):
            if i % 2 == 0:
                answer += v.upper()
            else:
                answer += v.lower()
        answer += ' '
    return answer


# 두번째 풀이 : split("") 이용하여 테스트 통과
def solution(s):
    answer = ''
    words = s.split()
    for w in words:
        for i, v in enumerate(w):
            if i % 2 == 0:
                answer += v.upper()
            else:
                answer += v.lower()
        answer += ' '
    return answer
