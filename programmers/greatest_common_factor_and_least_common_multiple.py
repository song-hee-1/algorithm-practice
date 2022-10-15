# 두 수를 입력받아 두 수의 최대공약수와 최소공배수를 반환하는 함수, solution을 완성해 보세요.
# 배열의 맨 앞에 최대공약수, 그다음 최소공배수를 넣어 반환하면 됩니다.
# 예를 들어 두 수 3, 12의 최대공약수는 3, 최소공배수는 12이므로 solution(3, 12)는 [3, 12]를 반환해야 합니다.


나의 풀이 : gcd 이용
from fractions import gcd
def solution(n, m):
    g = gcd(n, m)
    l = (n * m) // g
    return [g, l]

# 다른 사람의 풀이 : 유클리드 호제법
def solution(n, m):
    c, d = max(n, m), min(n, m)
    t = 1
    while t > 0:
        t = c % d
        c, d = d, t
    answer = [c, int(n*m/c)]

    return answer