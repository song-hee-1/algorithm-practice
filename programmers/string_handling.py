# 1-1. try-except문 -> 정확성 87.5점으로 테스트 실패
def solution_1(s):
    try:
        len_s = len(s)
        new_s = int(s)
    except ValueError:
        answer = False
    else:
        if len_s == 4 or 6:
            answer = True
        else:
            answer = False
    return answer


# 1-2. try-except문 코드 수정 -> 정확성 87.5점으로 테스트 실패
def solution_2(s):
    if len(s) == 4 or 6:
        try:
            int(s)
        except ValueError:
            return False
        else:
            return True


# 1-3. try-except문 코드 수정 -> 정확성 100점으로 테스트 통과
def solution_3(s):
    try:
        int(s)
    except ValueError:
        return False
    else:
        return len(s) == 4 or len(s) == 6


# 2. str.isdigit 메서드 이용
def solution_4(s):
    return s.isdigit() and len(s) in (4, 6)
