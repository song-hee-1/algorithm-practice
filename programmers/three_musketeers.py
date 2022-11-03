from itertools import combinations


def solution(number):
    combination = [sum(comb) for comb in list(combinations(number, 3)) if sum(comb) == 0]
    return len(combination)
