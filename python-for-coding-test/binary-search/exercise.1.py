# 이진 탐색
def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None

n = int(input())
array = list(map(int, input().split()))
array.sort()

m = int(input())
target = list(map(int, input().split()))

for t in target:
    result = binary_search(array, t, 0, n-1)
    if result != None:
        print('yes', end = ' ')
    else:
        print('no', end = ' ')


# 계수 정렬
n = int(input())
array = [0] * 1000001

for i in input().split():
    array[int(i)] = 1

m = int(input())
target = list(map(int, input().split()))

for t in target:
    if array[t] == 1:
        print('yes', end=' ')
    else:
        print('no', end=' ')
