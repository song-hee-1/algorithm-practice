# 정수를 저장한 배열, arr 에서 가장 작은 수를 제거한 배열을 리턴하는 함수, solution을 완성해주세요.
# 단, 리턴하려는 배열이 빈 배열인 경우엔 배열에 -1을 채워 리턴하세요.
# 예를들어 arr이 [4,3,2,1]인 경우는 [4,3,2]를 리턴 하고, [10]면 [-1]을 리턴 합니다.


# 나의 풀이: pop 이용
def solution(arr):
    if len(arr) == 1:
        return [-1]
    else:
        min_num = min(arr)
        arr.pop(arr.index(min_num))
        return arr


# Refactor : pop보다 del이 더 빠르므로 수
def solution(arr):
    if len(arr) == 1:
        return [-1]
    else:
        min_num = min(arr)
        del arr[arr.index(min_num)]
        return arr


# 다른 사람의 풀이 : list comprehension 이용 => 시간초과
# array의 크기만큼 for문을 돌기 때문에 시간복잡도가 큼
def solution(arr):
    if len(arr) == 1:
        return [i for i in arr if i > min(arr)]
    else:
        return [-1]


# 다른 사람의 풀이 : remove 이용
def solution(arr):
    if len(arr) > 1:
        arr.remove(min(arr))

        return arr
    else:
        return [-1]
