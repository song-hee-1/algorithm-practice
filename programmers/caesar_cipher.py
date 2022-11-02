def solution(s, n):
    answer = []
    for val in s:
        if val == ' ':
            answer.append(' ')
        else:
            if val.islower():  # 소문자일 경우
                answer.append(chr((ord(val) - ord('a') + n) % 26 + ord('a')))
            elif val.isupper():  # 대문자일 경우
                answer.append(chr((ord(val) - ord('A') + n) % 26 + ord('A')))

    return ''.join(answer)
