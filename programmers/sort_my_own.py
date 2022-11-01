# lambd를 이용하여 정렬 우선순위 설정
def solution(strings, n):
    return sorted(strings, key=lambda x: (x[n], x))
