import math


def solution(area):
    list_of_area = []
    result = solution_generator(area, list_of_area)
    return result


def solution_generator(n, list_of_area):
    square_root = math.sqrt(n)
    if type(square_root) == float:
        square_root = int(square_root)

    area = square_root*square_root
    list_of_area.append(area)
    n = n-area
    if n > 3:
        return solution_generator(n, list_of_area)
    else:
        list_of_area.extend([1 for x in range(n)])
        return list_of_area


print(solution(15324))
