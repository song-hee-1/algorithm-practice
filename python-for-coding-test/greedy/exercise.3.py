# Q. 어떠한 수 N이 1이 될 때까지 다음의 두 과정 중 하나를 반복적으로 선택하여 수행하려고 한다. 단, 두번째 연산은 N이 K로 나누어떨어질 때만 선택할 수 있다.
# 1. N에서 1을 뺀다.  2. N을 K로 나눈다.
# N과 K가 주어질 때 N이 1이 될 때까지 1번 혹은 2번의 과정을 수행해야 하는 최소 횟수를 구하는 프로그램을 작성하시오.

# 단순하게 풀었을 때
n, k = map(int, input().split())
result = 0

while n >= k:
    # N이 K로 나누어 떨어지지 않는다면 N에서 1빼기
    while n % k != 0:
        n -= 1
        result += 1
    # N이 K로 나누어 떨어진다면 그 때의 몫 구하기
    n //= k
    result += 1

while n > 1:
    n -= 1
    result += 1

print(result)

# N이 100억 이상의 큰 수가 되는 경우에도 빠르게 동작하기 위해 N이 K의 배수가 되도록 효율적으로 한 번에 빼는 방식
n, k = map(int, input().split())
result = 0

while True:
    # N == K로 나누어지는 수가 될 때까지 1씩 빼기
    target = (n // k) * k
    result += (n - target)
    n = target
    # n이 k보다 작아 더 이상 나눌 수 없을 때 반복 탈출
    if n < k:
        break
    result += 1
    n //= k

result += (n - 1)
print(result)
