# 필요한 구명보트 개수의 최솟값을 구하기 위해서 몸무게가 적은 사람 2명끼리 묶어 한 배를 태우면 된다고 생각하고 풀었으나,
# 가장 몸무게가 큰 사람과 가장 몸무게가 적은 사람을 묶어 한 배에 태워야 해야 정답이었다.


def solution(people, limit):
    people.sort(reverse=True)
    if people[-1] + people[-2] > limit:
        return len(people)
    else:
        return len(people) - 1


def solution2(people, limit):
    answer = 0
    people.sort()

    start, end = 0, len(people) - 1

    while start <= end:
        answer += 1
        if people[start] + people[end] <= limit:
            start += 1
        end -= 1

    return answer
