# 나의 풀이 : 3진법 표현에서 3의 배수일 때 몫에서 1씩 빼주기
def solution(n):
    answer = ''
    while n:
        if n % 3 == 0:
            answer = str(4) + answer
            n = n//3 - 1
        else:
            answer = str(n % 3) + answer
            n = n // 3
    return answer


# 가장 많은 좋아요를 받은 풀이
def change124(n):
    num = ['1', '2', '4']
    answer = ""

    while n > 0:
        n -= 1
        answer = num[n % 3] + answer
        n //= 3

    return answer
