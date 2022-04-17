def solution(array, commands):
    start = 0
    answer = []
    for _ in range(len(commands)):
        i = commands[start][0]
        j = commands[start][1]
        k = commands[start][2]
        new_array = array[i-1:j]
        new_array.sort()
        print(new_array)
        num = new_array[k-1]
        print(num)
        answer.append(num)
        start += 1
    return answer


