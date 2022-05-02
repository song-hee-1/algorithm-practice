# Q. 여러 개의 숫자 카드 중에서 가장 높은 숫자가 쓰인 카드 한 장을 뽑아야 한다.
#     단, 먼저 뽑고자 하는 카드가 포함되어 있는 행을 선택한 후 선택된 행에 포함된 카드들 중 가장 숫자가 낮은 카드를 뽑아야 한다.

# min() 이용
n, m = map(int, input().split())

result = 0

for i in range(n):
    data = list(map(int, input().split()))
    min_value = min(data)
    result = max(result, min_value)

print(result)


# 2중 반복문 구조 이용
n, m = map(int, input().split())

result = 0

for i in range(n):
    data = list(map(int, input().split()))
    # 비교를 위해 임의의 큰 수 지정
    min_value = 10001
    for a in data:
        min_value = min(min_value, a)
    result = max(result, min_value)

print(result)
