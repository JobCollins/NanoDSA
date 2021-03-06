# def smallest_integer(array_data):
#     array_data = array_data
#     max_val = max(array_data)
#     num_list = []

#     [num_list.append(i) for i in range(max_val) if i not in array_data and i > 0]

#     return min(num_list)

# print(smallest_integer([1,3,6,4, 1, 2]))

# def test():
#     assert smallest_integer([1,3,6,4, 1, 2]) == 5
#     assert smallest_integer ([10000, 3, -1, -3, 1000000]) == 1

# for i in range(5):
#     print(i*'* ')
#     print('\n')

# print(50//10)

# def decimals(n):
#     result=0
#     while n > 0:
#         n = n // 10
#         result += 1
#     return result

# def fibonnacci(n):
#     a=0
#     b=1
#     while a <= n:
#         print(a)
#         c = a + b
#         a = b
#         b = c
#     return a

# def binary_gap(n):
#     binary_str = str(bin(n)[2:])

#     # largest binary gap variable
#     max_count = None
#     #characters count in a given binary string
#     this_count = 0
#     # check if the previous character is a zero
#     prev_char_zero = None

#     for character in binary_str:
#         # check whether character is a zero
#         is_zero_char = character =='0'
#         print(character, is_zero_char)
#         print("bool: ", bool(prev_char_zero), "bool cond: ", bool(prev_char_zero) != bool(is_zero_char))

#         # if the previous character is not a zero
#         if bool(prev_char_zero) != bool(is_zero_char):
#             if max_count is None:
#                 max_count = 0
#             #save the biggest binary gap
#             elif this_count> max_count:
#                 print('this count: ', this_count)
#                 max_count = this_count
#             # reset the count
#             this_count = 1
#         else:
#             # increment the length of the sequenve
#             this_count += 1

#         # track what the previous character was
#         prev_char_zero = is_zero_char
#     print( "%s: %s = %s" % (n, binary_str, max_count))
#     if max_count is not None:
#         return max_count
#     else:
#         return 0

# print(binary_gap(32))

def solution(A):
    """
    Find the value that does not have a match in an odd sized array
    :param A: an array of integers with an odd number of elements
    :param N: length of the array
    :return: the one element which does not have a complementary element
    """

    # dictionary of keys in need of a match
    unmatched = dict()

    # for every element
    for element in A:
        # try removing it's match
        try:
            del unmatched[element]
        except KeyError:
            # else add it
            unmatched[element] = True
    print(unmatched)
    # if one unmatched item
    if len(unmatched) == 1:
        item = list(unmatched.keys())[0]
        return item
    else:
        raise Exception("Expected one unmatched item, but have this: %s" % unmatched)

def reverse(A):
    n = len(A)
    for i in range(n//2):
        k = n - i -  1
        A[i], A[k] = A[k], A[i]
    return A

def rotate(A):
    # counter = 1
    for i in range(3):
        B = [None]*len(A)
        for j in range(len(A)):
            B[j] = A[j-1]
        A = B
    return A

print(rotate([3,8,9,7,6]))

