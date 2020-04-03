def solution(A):
    sum_num=0
    for i in range(len(A)-1):
        if(A[i]==A[i+1]):
            flag=0
            for k in range(i,0,-1):
                if(A[k]==A[k-1]):
                    flag=k
            min_num = i-flag+1
            flag=len(A)
            for k in range(i,len(A)-1):
                if(A[k]==A[k+1]):
                    flag=k
            if min_num > flag-i+1:
                sum_num = sum_num + min_num
            else:
                sum_num = sum_num + flag-i+1
    return sum_num
