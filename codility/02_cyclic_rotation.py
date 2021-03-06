def solution(A, k):
    """
    given an array A consisting of N integers and an integer K, 
    returns the array A rotated K times
    """
    for i in range(k):
        B = [None]*len(A)
        for j in range(len(A)):
            B[j] = A[j-1]
        A = B
    return A

# print(solution([3,8,9,7,6], 3))

def solution_diff_rotation(A, k):
    """
    given an array A consisting of N integers and an integer K, 
    returns the array A rotated K times
    """
    for i in range(k):
        B = [None]*len(A)
        last = A[0]
        print("last, ",last)
        for j in range(len(A)):
            try:
                B[j] = A[j+1]
            except IndexError:
                B[j] = last
        A = B
    return A
print(solution_diff_rotation([3,8,9,7,6], 5))
