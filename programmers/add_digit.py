# str과 int변환을 이용한 나의 풀이
def solution(n):
    str_n = str(n)
    dsum = 0
    for digit in str_n:
        dsum += int(digit)
    return dsum


# 재귀구조를 이용해 가장 많은 좋아요를 받은 풀이
def sum_digit(number):
    if number < 10:
        return number
    return (number % 10) + sum_digit(number // 10)
