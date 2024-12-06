def solution(n):
    answer = [1, 2] * (n)
    
    for i in range(2, n):
        answer[i] = (answer[i-1] + answer[i-2])
    return answer[n-1] % 1234567