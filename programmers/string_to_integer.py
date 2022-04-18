#Built-in Functions:int() 이용
def solution(s):
    return int(s)

#int()이용하지 않았을 때
def strToInt(str):
    result = 0

    for idx, number in enumerate(str[::-1]):
        if number == '-':
            result *= -1
        elif number == '+':
            pass
        else:
            result += int(number) * (10 ** idx)

    return result


# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(solution("-1234"))
print(solution("+1234"))
print(strToInt("-1234"))
print(strToInt("+1234"))