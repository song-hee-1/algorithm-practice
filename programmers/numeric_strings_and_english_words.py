def solution(s):
    word = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    for idx, string in enumerate(word):
        if string in s:
            s = s.replace(string, str(idx))
    return int(s)