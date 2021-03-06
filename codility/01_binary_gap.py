def solution(n):
    # print(bin(n))
    binary_str = str(bin(n)[2:])

    return len(max(binary_str.strip('0').strip('1').split('1')))

print(solution(1041))
# binary_str = str(bin(529)[2:])
# print(binary_str.strip('0').strip('1').split('1'))