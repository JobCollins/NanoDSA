# An array A consisting of N different integers is given. 
# The array contains integers in the range [1..(N + 1)], 
# which means that exactly one element is missing.
# Find that missing element.

def solution(A):
    n = len(A) + 1
    total = n * (n+1) //2  #sum of natural numbers
    return total - sum(A) #the difference is the missing number

print(solution([2,3,1,5]))