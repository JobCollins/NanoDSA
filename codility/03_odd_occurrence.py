def solution(A):
    """
    given an array A consisting of N integers of odd
    number of elements, each element can be paired with
    another element that has same value, except for one 
    that is left unpaired, returns the value of the unpaired element.
    """
    # for element in A:
    #     if bool(A.count(element) % 2 == 0):
    #         pass
    #     else:
    #         return element
    # bad complexity O(n^2)
    
    paired = dict.fromkeys(A, 0)
    # print("Before: ", paired)

    for element in A:
        paired[element] += 1
    
    for k,v in paired.items():
        if v % 2 == 1:
            return k



print(solution([9,3,9,3,9,7,9]))
