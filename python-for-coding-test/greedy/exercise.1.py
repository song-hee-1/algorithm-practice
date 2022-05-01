# Q. 다양한 수로 이루어진 배열이 있을 때 주어진 수들을 m번 더하여 가장 큰 수를 만들어라.
# 단, 배열의 특정한 인덱스에 해당하는 수가 연속해서 K번을 초과하여 더해질 수 없다.

# 단순하게 풀었을 때
n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort()
first_max = data[n-1]
second_max = data[n-2]

result = 0

while True:
    for i in range(k):
        if m == 0:
            break
        result += first_max
        m -= 1
    if m == 0:
        break
    result += second_max
    m -= 1

print(result)

# int(m / (k + 1)) * k + m % (k + 1)의 수학적 아이디어를 이용하여 풀었을 때
n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort()
first_max = data[n-1]
second_max = data[n-2]

# 가장 큰 수가 더해지는 횟수 계산
count = int(m / (k+1)) * k
count += m % (k+1)

result = 0
result += count * first_max
result += (m - count) * second_max

print(result)
