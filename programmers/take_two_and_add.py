def solution(numbers):
    answer = []

    for i in range(len(numbers) - 1):
        for j in range(i + 1, len(numbers)):
            answer.append(numbers[i] + numbers[j])

    answer = sorted(list(set(answer)))

    return answer

# 파이썬의 set 자료구조는 중복이 없다는 특징을 가지고 있으므로, 이를 이용하여 중복된 값을 제거할 수 있다.
