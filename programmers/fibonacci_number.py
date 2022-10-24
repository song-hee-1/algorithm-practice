def solution(n):
    answer = 0
    fibo_num_list = [0, 1]

    for i in range(n - 1):
        fibo_num_list.append(fibo_num_list[i] + fibo_num_list[i + 1])

    return fibo_num_list[n] % 1234567
