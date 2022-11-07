"""
Alice and Bob work in a beautiful orchard. There are N apple trees in the orchard. The apple trees are arranged in a row and they are numbered from 1 to N.
Alice is planning to collect all the apples from K consecutive trees and Bob is planning to collect all the apples from L consecutive trees.
They want to choose to disjoint segements (one consisting of K trees of Alice and the other consisting of L trees for Bob) so as not to disturb each other. you should return the maximum number of apples that they can collect.
    N is an integer within the range: [2, 600]
    K and L are integers within the range: [1, N - 1]
    each element of array A is an integer within the range: [1, 500]

Example

Example 1:

input:
A = [6, 1, 4, 6, 3, 2, 7, 4]
K = 3
L = 2
Output:
24
Explanation:
beacuse Alice can choose tree 3 to 5 and collect 4 + 6 + 3 = 13 apples, and Bob can choose trees 7 to 8 and collect 7 + 4 = 11 apples.Thus, they will collect 13 + 11 = 24.

Example 2:

Input:
A = [10, 19, 15]
K = 2
L = 2
Output:
-1
Explanation:
beacause it is not possible for Alice and Bob to choose two disjoint intervals.
"""


def calculate_max_sum_based_on_steps_sequence(a, m, n):
    result = 0
    max_sum_of_m = 0
    d = []

    for i in range(0, len(a)-m+1):
        temp_sum_of_m = sum(a[i:i+m])
        if temp_sum_of_m > max_sum_of_m:
            max_sum_of_m = temp_sum_of_m
            d = [iii for iii in range(i, i+m)]

        max_sum_of_n = 0
        for j in range(0, len(a)-n+1):
            if not {ii for ii in range(i, i+m)}.intersection({jj for jj in range(j, j+n)}) and not set(d).intersection({jj for jj in range(j, j+n)}):
                temp_sum_of_n = sum(a[j:j + n])
                if temp_sum_of_n > max_sum_of_n and max_sum_of_m + temp_sum_of_n:
                    max_sum_of_n = temp_sum_of_n

        if max_sum_of_m + max_sum_of_n > result:
            result = max_sum_of_m + max_sum_of_n
    return result


def solution(a, m, n):
    if m+n > len(a):
        return -1

    if m+n == len(a):
        return sum(a)

    max_num_first = calculate_max_sum_based_on_steps_sequence(a, m, n)
    min_num_first = calculate_max_sum_based_on_steps_sequence(a, n, m)
    return max(max_num_first, min_num_first)


print(solution([6, 1, 4, 6, 3, 2, 7, 4], 3, 2))
