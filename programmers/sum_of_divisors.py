#for문 이용
def solution1(n):
    sum_div = 0
    for i in range(1, n+1):
        if n % i == 0:
            sum_div += i
    return sum_div

#list comprehension 이용
def solution2(n):
    return sum([i for i in range(1, n+1) if n % i == 0])

#num //2 이용 -> 제일 빠른 실행속도
def solution3(n):
    return n + sum([i for i in range(1, (n // 2) + 1) if n % i == 0])
