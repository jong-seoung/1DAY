def solution(arr1, arr2):
    answer = []
    for i, j in zip(arr1, arr2):
        ans = []
        for l, m in zip(i,j):
            ans.append(l+m)
        answer.append(ans)
    return answer