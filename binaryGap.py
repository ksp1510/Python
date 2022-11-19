def solution(N):
    # write your code in Python 3.8.10
    maxn = 0
    cnt = 0
    flag = 0
    while(N != 0):
        if((N & 1) == 1 and flag == 0):
            flag = 1
            N >>= 1
        elif((N & 1) == 0 and flag == 0):
            N >>= 1
        elif((N & 1) == 0 and flag == 1):
            cnt += 1
            N >>= 1
        elif((N & 1) == 1 and flag == 1):
            maxn = max(maxn, cnt)
            cnt = 0
            flag = 0
    return maxn
