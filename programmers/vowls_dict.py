from itertools import product
def solution(word):
    dict = []
    for i in range(1, 6):
        dict.extend((list(map(''.join, product(['A', 'E', 'I', 'O', 'U'], repeat = i)))))
    dict.sort()
    return dict.index(word)+1