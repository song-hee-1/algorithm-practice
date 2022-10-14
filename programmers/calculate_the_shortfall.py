# 입출력 예
# price	money	count	result
# 3	    20	    4	    10
# 입출력 예 설명

# 이용금액이 3인 놀이기구를 4번 타고 싶은 고객이 현재 가진 금액이 20이라면, 총 필요한 놀이기구의 이용 금액은 30 (= 3+6+9+12) 이 되어
# 10만큼 부족하므로 10을 return 합니다.

# 나의 풀이 : for loop 이용
def solution(price, money, count):
    usage_amount = 0
    for i in range(1, count + 1):
        usage_amount += price * i
    if money >= usage_amount:
        return 0
    else:
        return abs(money - usage_amount)


# 다른 사람의 풀이 : 산술평균 이용
def solution(price, money, count):
    return max(0, price * (count + 1) * count // 2 - money)


# 다른 사람의 풀이 : list comprehension 이용 (if문 대신 min()으로 부족한 금액이 양수일때는 0, 음수일때는 절댓값 적용)
def solution(price, money, count):
    return abs(min(money - sum([price * i for i in range(1, count + 1)]), 0))
