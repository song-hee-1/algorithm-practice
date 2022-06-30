# 나의 풀이 => 통과
def solution(s):
    a = list(map(int, s.split()))
    answer_list = []
    answer_list.append(max(a))
    answer_list.append(min(a))
    answer_list.sort()
    return ' '.join(map(str,answer_list))


# 가장 많은 좋아요를 받은 풀이
def solution(s):
    s = list(map(int,s.split()))
    return str(min(s)) + " " + str(max(s))

# answer_list를 만들지 않고 바로 최대,최소값을 return하면 된다는 점을 배웠다.